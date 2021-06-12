import mechanize
import ssl
import http.cookiejar

### Variables ---------------------------------------------
printResponses = False
### End variables -----------------------------------------

class ConsoleColors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Handle SSL certification context
try:
    make_non_ssl_context = ssl._create_verified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = make_non_ssl


def print_response(response):
    if(printResponses):
        print("Got response: " + ConsoleColors.YELLOW)
        for r in response:
            print(r)
        print(ConsoleColors.RESET)

def validate_hack(inputString, response):
    for r in response:
        if( inputString in str(r) ):
            print( ConsoleColors.GREEN + "\t> Found in response: "  + ConsoleColors.RESET + str(r))
            return True
    return False


# Initialize mechanize browser
br = mechanize.Browser()
# Set cookie Jar
cj = http.cookiejar.LWPCookieJar()
br.set_cookiejar(cj)
# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
# Initialize mechanize bot on localhost website
br.set_handle_robots(False)
br.open("http://localhost:8000/")



# ---------------------------------------------------------
#   BOT 1    ----------------------------------------------
#       Targets nth form on site          -----------------
#       fills all the fields and submits    ---------------
# ---------------------------------------------------------
def run_bot_1(selectedForm : int):
    formControls = []
    br.select_form(nr=selectedForm)
    for control in br.forms()[selectedForm].controls:
        formControls.append(control.name)
    for control in formControls:
        if control != None:
            if not br.form.find_control(control).readonly:
                try:
                    br.form[control] = "HaCkEd"
                except TypeError:
                    pass
    try:
        res = br.submit()
        if res:
            print_response(res)
            if( validate_hack("HaCkEd", res) ):
                print(ConsoleColors.GREEN + "\tBot SUCCEEDED!" + ConsoleColors.RESET)
                return True
            else:
                print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Respond does not contain input variables.")
        else:
            print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Got no response.")
    except:
        print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Could not submit.")
    return False


print("[" + ConsoleColors.CYAN + "BOT 1 - UNIVERSAL"  + ConsoleColors.RESET + "] Running on form 0: ")
run_bot_1(0)
print("[" + ConsoleColors.CYAN + "BOT 1 - UNIVERSAL"  + ConsoleColors.RESET + "] Running on form 2: ")
run_bot_1(2)


# ---------------------------------------------------------
#   BOT 2    ----------------------------------------------
#       Finds control with a given name          ----------
#       in form with a given index number        ----------
# ---------------------------------------------------------
def run_bot_2(selectedForm : int, controlNames = []):
    formControls = []
    br.select_form(nr=selectedForm)
    for controlName in controlNames:
        try:
            controlFound = br.form.find_control(controlName)
            if controlFound != None:
                if not controlFound.readonly:
                    try:
                        br.form[controlFound.name] = "HaCkEd"
                    except TypeError:
                        pass
        except mechanize._form_controls.ControlNotFoundError:
            pass
    try:
        res = br.submit()
        if res:
            print_response(res)
            if( validate_hack("HaCkEd", res) ):
                print(ConsoleColors.GREEN + "\tBot SUCCEEDED!" + ConsoleColors.RESET)
                return True
            else:
                print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Respond does not contain input variables.")
        else:
            print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Got no response.")
    except:
        print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Could not submit.")
    return False

print("[" + ConsoleColors.CYAN + "BOT 2 - UNIVERSAL"  + ConsoleColors.RESET + "] Running on form 0: ")
run_bot_2(0, ["fname", "lname"])
run_bot_2(0, ["fname"])
run_bot_2(0, ["lname"])
print("[" + ConsoleColors.PURPLE + "BOT 2 - SITE SPECIALIZED"  + ConsoleColors.RESET + "] Running on form 2: ")
run_bot_2(2, ["color", "number", "date"])
run_bot_2(2, ["color"])
run_bot_2(2, ["number"])
run_bot_2(2, ["date"])


# ---------------------------------------------------------
#   BOT 3    ----------------------------------------------
#       Finds form and control with a given name ----------
# ---------------------------------------------------------
def run_bot_3(formName = "", controlNames = []):
    formControls = []
    br.select_form(name=formName)
    for controlName in controlNames:
        try:
            controlFound = br.form.find_control(controlName)
            if controlFound != None:
                if not controlFound.readonly:
                    try:
                        br.form[controlFound.name] = "HaCkEd"
                    except TypeError:
                        pass
        except mechanize._form_controls.ControlNotFoundError:
            pass
    try:
        res = br.submit()
        if res:
            print_response(res)
            if( validate_hack("HaCkEd", res) ):
                print(ConsoleColors.GREEN + "\tBot SUCCEEDED!" + ConsoleColors.RESET)
                return True
            else:
                print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Respond does not contain input variables.")
        else:
            print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Got no response.")
    except:
        print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Could not submit.")
    return False


print("[" + ConsoleColors.PURPLE + "BOT 3 - SITE SPECIALIZED"  + ConsoleColors.RESET + "] Running on form 'nameform': ")
run_bot_3("nameform", ["fname", "lname"])
run_bot_3("nameform", ["fname"])
run_bot_3("nameform", ["lname"])

print("[" + ConsoleColors.PURPLE + "BOT 3 - SITE SPECIALIZED"  + ConsoleColors.RESET + "] Running on form 'otherform': ")
run_bot_3("otherform", ["number", "date", "color"])
run_bot_3("otherform", ["number"])
run_bot_3("otherform", ["date"])
run_bot_3("otherform", ["color"])


# ---------------------------------------------------------
#   BOT 4    ----------------------------------------------
#       Finds form with a specific class    ---------------
#       and fills all the data in controls    -------------
# ---------------------------------------------------------
def run_bot_4(className = ""):
    formControls = []
    br.select_form(class_=lambda x: className in x)
    for control in br.form.controls:
        formControls.append(control.name)
    for control in formControls:
        if control != None:
            if not br.form.find_control(control).readonly:
                try:
                    br.form[control] = "HaCkEd"
                except TypeError:
                    pass
    try:
        res = br.submit()
        if res:
            print_response(res)
            if( validate_hack("HaCkEd", res) ):
                print(ConsoleColors.GREEN + "\tBot SUCCEEDED!" + ConsoleColors.RESET)
                return True
            else:
                print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Respond does not contain input variables.")
        else:
            print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Got no response.")
    except:
        print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Could not submit.")
    return False

print("[" + ConsoleColors.PURPLE + "BOT 4 - SITE SPECIALIZED"  + ConsoleColors.RESET + "] Running on form with class 'customformclass1': ")
run_bot_4("customformclass1")
print("[" + ConsoleColors.PURPLE + "BOT 4 - SITE SPECIALIZED"  + ConsoleColors.RESET + "] Running on form with class 'customformclass3': ")
run_bot_4("customformclass3")


# ---------------------------------------------------------
#   BOT 5    ----------------------------------------------
#       Finds form with a specific class    ---------------
#       and specified controlNames          ---------------
# ---------------------------------------------------------
def run_bot_5(className = "", controlNames = []):
    formControls = []
    br.select_form(class_=lambda x: className in x)
    for controlName in controlNames:
        try:
            controlFound = br.form.find_control(controlName)
            if controlFound != None:
                if not controlFound.readonly:
                    try:
                        br.form[controlFound.name] = "HaCkEd"
                    except TypeError:
                        pass
        except mechanize._form_controls.ControlNotFoundError:
            pass
    try:
        res = br.submit()
        if res:
            print_response(res)
            if( validate_hack("HaCkEd", res) ):
                print(ConsoleColors.GREEN + "\tBot SUCCEEDED!" + ConsoleColors.RESET)
                return True
            else:
                print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Respond does not contain input variables.")
        else:
            print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Got no response.")
    except:
        print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Could not submit.")
    return False


print("[" + ConsoleColors.PURPLE + "BOT 5 - SITE SPECIALIZED"  + ConsoleColors.RESET + "] Running on form with class 'customformclass1': ")
run_bot_5("customformclass1", ["fname", "lname"])
run_bot_5("customformclass1", ["fname"])
run_bot_5("customformclass1", ["lname"])

print("[" + ConsoleColors.PURPLE + "BOT 5 - SITE SPECIALIZED"  + ConsoleColors.RESET + "] Running on form with class 'customformclass3': ")
run_bot_5("customformclass3", ["number", "date", "color"])
run_bot_5("customformclass3", ["number"])
run_bot_5("customformclass3", ["date"])
run_bot_5("customformclass3", ["color"])
