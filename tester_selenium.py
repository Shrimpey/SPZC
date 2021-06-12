from selenium import webdriver
import selenium
from webdriver_manager.chrome import ChromeDriverManager

driver = selenium.webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://127.0.0.1:8000')


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


def was_successful(formId = 0, hackText = "HaCkEd"):
    result = driver.find_element_by_name("result1")
    if(formId == 1):
        result = driver.find_element_by_name("result2")
    elif(formId == 2):
        result = driver.find_element_by_name("result3")
    innerHTML = result.get_attribute('innerHTML')
    print("\t> Got result: " + ConsoleColors.YELLOW + innerHTML + ConsoleColors.RESET)
    if str(hackText) in innerHTML:
        return True
    return False



# ---------------------------------------------------------
#   BOT 1    ----------------------------------------------
#       Searches for controls by id          --------------
#       and submit button by id              --------------
# ---------------------------------------------------------
def run_bot_1(selectedForm : int, controlNames = [], submitIndex = 0, hackText = "HaCkEd"):
    try:
        for controlName in controlNames:
            fname = driver.find_element_by_id(controlName)
            fname.clear()
            fname.send_keys(hackText)
        try:
            driver.find_elements_by_id("submit")[submitIndex].click()
        except IndexError:
            print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Could not find submit button.")
            return
        if was_successful(selectedForm, hackText):
            print(ConsoleColors.GREEN + "\tBot SUCCEEDED!" + ConsoleColors.RESET)
        else:
            print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Respond does not contain input variables.")
    except selenium.common.exceptions.NoSuchElementException:
        print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Could not find element.")

print("[" + ConsoleColors.CYAN + "BOT 1 - UNIVERSAL"  + ConsoleColors.RESET + "] Running on form 0: ")
run_bot_1(0, ["fname", "lname"])
run_bot_1(0, ["fname"])
run_bot_1(0, ["lname"])

print("[" + ConsoleColors.PURPLE + "BOT 1 - SPECIALIZED"  + ConsoleColors.RESET + "] Running on form 2: ")
run_bot_1(2, ["number"], 2, "99")
run_bot_1(2, ["color"], 2, "#abcabc")


# ---------------------------------------------------------
#   BOT 2    ----------------------------------------------
#       Searches for controls by name          --------------
#       and submit button by id              --------------
# ---------------------------------------------------------
def run_bot_2(selectedForm : int, controlNames = [], submitIndex = 0, hackText = "HaCkEd"):
    try:
        for controlName in controlNames:
            fname = driver.find_element_by_name(controlName)
            fname.clear()
            fname.send_keys(hackText)
        try:
            driver.find_elements_by_id("submit")[submitIndex].click()
        except IndexError:
            print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Could not find submit button.")
            return
        if was_successful(selectedForm, hackText):
            print(ConsoleColors.GREEN + "\tBot SUCCEEDED!" + ConsoleColors.RESET)
        else:
            print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Respond does not contain input variables.")
    except selenium.common.exceptions.NoSuchElementException:
        print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Could not find element.")

print("[" + ConsoleColors.CYAN + "BOT 2 - UNIVERSAL"  + ConsoleColors.RESET + "] Running on form 0: ")
run_bot_2(0, ["fname", "lname"])
run_bot_2(0, ["fname"])
run_bot_2(0, ["lname"])

print("[" + ConsoleColors.PURPLE + "BOT 2 - SPECIALIZED"  + ConsoleColors.RESET + "] Running on form 2: ")
run_bot_2(2, ["number"], 2, "99")
run_bot_2(2, ["color"], 2, "#abcabc")


# ---------------------------------------------------------
#   BOT 3    ----------------------------------------------
#       Searches for controls by id          --------------
#       and submit button by classname       --------------
# ---------------------------------------------------------
def run_bot_3(selectedForm : int, controlNames = [], submitIndex = 0, hackText = "HaCkEd"):
    try:
        for controlName in controlNames:
            fname = driver.find_element_by_id(controlName)
            fname.clear()
            fname.send_keys(hackText)
        try:
            driver.find_elements_by_class_name("submitbuttonclass")[submitIndex].click()
        except IndexError:
            print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Could not find submit button.")
            return
        if was_successful(selectedForm, hackText):
            print(ConsoleColors.GREEN + "\tBot SUCCEEDED!" + ConsoleColors.RESET)
        else:
            print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Respond does not contain input variables.")
    except selenium.common.exceptions.NoSuchElementException:
        print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Could not find element.")

print("[" + ConsoleColors.CYAN + "BOT 3 - UNIVERSAL"  + ConsoleColors.RESET + "] Running on form 0: ")
run_bot_3(0, ["fname", "lname"])
run_bot_3(0, ["fname"])
run_bot_3(0, ["lname"])

print("[" + ConsoleColors.PURPLE + "BOT 3 - SPECIALIZED"  + ConsoleColors.RESET + "] Running on form 2: ")
run_bot_3(2, ["number"], 2, "99")
run_bot_3(2, ["color"], 2, "#abcabc")


# ---------------------------------------------------------
#   BOT 4    ----------------------------------------------
#       Searches for controls by name          --------------
#       and submit button class name           --------------
# ---------------------------------------------------------
def run_bot_4(selectedForm : int, controlNames = [], submitIndex = 0, hackText = "HaCkEd"):
    try:
        for controlName in controlNames:
            fname = driver.find_element_by_name(controlName)
            fname.clear()
            fname.send_keys(hackText)
        try:
            driver.find_elements_by_class_name("submitbuttonclass")[submitIndex].click()
        except IndexError:
            print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Could not find submit button.")
            return
        if was_successful(selectedForm, hackText):
            print(ConsoleColors.GREEN + "\tBot SUCCEEDED!" + ConsoleColors.RESET)
        else:
            print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Respond does not contain input variables.")
    except selenium.common.exceptions.NoSuchElementException:
        print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Could not find element.")

print("[" + ConsoleColors.CYAN + "BOT 4 - UNIVERSAL"  + ConsoleColors.RESET + "] Running on form 0: ")
run_bot_4(0, ["fname", "lname"])
run_bot_4(0, ["fname"])
run_bot_4(0, ["lname"])

print("[" + ConsoleColors.PURPLE + "BOT 4 - SPECIALIZED"  + ConsoleColors.RESET + "] Running on form 2: ")
run_bot_4(2, ["number"], 2, "99")
run_bot_4(2, ["color"], 2, "#abcabc")
