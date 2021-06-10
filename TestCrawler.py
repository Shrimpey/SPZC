import mechanize
import ssl
import http.cookiejar

try:
    make_non_ssl_context = ssl._create_verified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = make_non_ssl


### Variables ---------------------------------------------
printResponses = False
### End variables -----------------------------------------


br = mechanize.Browser()

# Cookie Jar
cj = http.cookiejar.LWPCookieJar()
br.set_cookiejar(cj)


# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Initialize mechanize bot on localhost website
br.set_handle_robots(False)
br.open("http://localhost:8000/")

def PrintResponse(response):
    if(printResponses):
        print("Got response: \u001b[33m")
        for r in response:
            print(r)
        print("\u001b[0m")

def ValidadeHack(inputString, response):
    for r in response:
        if( inputString in str(r) ):
            print("\t> Found in response: " + str(r))
            return True
    return False


# ---------------------------------------------------------
# Bot 1A - Scans website for any forms  -------------------
#   Target: input text forms            -------------------
#   Complexity: moderate                -------------------
# ---------------------------------------------------------
print("Running bot 1A (lname, fname scanner)...")
formNames = []
for form in br.forms():
    for control in form.controls:
        formNames.append(control.name)
br.select_form(nr=0)
br.form[formNames[0]] = 'HACK1'
br.form[formNames[1]] = 'HACK2'
res = br.submit()
if res:
    PrintResponse(res)
    if( ValidadeHack("Chosen name: HACK1 HACK2", res) ):
        print("\u001b[32m Bot SUCCEEDED! \u001b[0m")
    else:
        print("\u001b[31m Bot FAILED! Respond does not contain input variables. \u001b[0m")
else:
    print("\u001b[31m Bot FAILED! Got no response. \u001b[0m")
print("---------------------")


# ---------------------------------------------------------
# Bot 1B - Scans website for any forms  -------------------
#   Target: radio control               -------------------
#   Complexity: moderate                -------------------
# ---------------------------------------------------------
print("Running bot 1B (pizza scanner)...")
formNames.clear()
selectedForm = 1
for control in br.forms()[selectedForm].controls:
    formNames.append(control.name)
br.select_form(nr=selectedForm)
br.form.find_control(formNames[0]).get("pizza").selected = True
res = br.submit()
if res:
    PrintResponse(res)
    if( ValidadeHack("Chosen food: pizza", res) ):
        print("\u001b[32m Bot SUCCEEDED! \u001b[0m")
    else:
        print("\u001b[31m Bot FAILED! Respond does not contain input variables. \u001b[0m")
else:
    print("\u001b[31m Bot FAILED! Got no response. \u001b[0m")

print("---------------------")


# ---------------------------------------------------------
# Bot 1C - Scans website for any forms  -------------------
#   Target: color, number, date         -------------------
#   Complexity: moderate                -------------------
# ---------------------------------------------------------
print("Running bot 1C (color, date, number scanner)...")
formNames.clear()
selectedForm = 2
for control in br.forms()[selectedForm].controls:
    formNames.append(control.name)
br.select_form(nr=selectedForm)
br.form[formNames[0]] = "#666"
br.form[formNames[1]] = "31-01-1997"
br.form[formNames[2]] = "66"
res = br.submit()
if res:
    PrintResponse(res)
    if( ValidadeHack("Chosen options: #666, 31-01-1997, 66", res) ):
        print("\u001b[32m Bot SUCCEEDED! \u001b[0m")
    else:
        print("\u001b[31m Bot FAILED! Respond does not contain input variables. \u001b[0m")
else:
    print("\u001b[31m Bot FAILED! Got no response. \u001b[0m")
print("---------------------")












# ---------------------------------------------------------
# Bot 2A - Scans for named forms        -------------------
#   Target: input text forms            -------------------
#   Complexity: simple                  -------------------
# ---------------------------------------------------------
print("Running bot 2A (lname, fname scanner)...")
br.select_form(nr=0)
try:
    br.form['fname'] = 'HACK1'
    br.form['lname'] = 'HACK2'
    res = br.submit()
    if res:
        PrintResponse(res)
        if( ValidadeHack("Chosen name: HACK1 HACK2", res) ):
            print("\u001b[32m Bot SUCCEEDED! \u001b[0m")
        else:
            print("\u001b[31m Bot FAILED! Respond does not contain input variables. \u001b[0m")
    else:
        print("\u001b[31m Bot FAILED! Got no response. \u001b[0m")
except mechanize._form_controls.ControlNotFoundError:
    print("\u001b[31m Bot FAILED! Got no response. \u001b[0m")
print("---------------------")


# ---------------------------------------------------------
# Bot 2B - Scans for named forms        -------------------
#   Target: radio control               -------------------
#   Complexity: simple                  -------------------
# ---------------------------------------------------------
print("Running bot 2B (pizza scanner)...")
br.select_form(nr=1)
try:
    br.form.find_control("food").get("pizza").selected = True
    res = br.submit()
    if res:
        PrintResponse(res)
        if( ValidadeHack("Chosen food: pizza", res) ):
            print("\u001b[32m Bot SUCCEEDED! \u001b[0m")
        else:
            print("\u001b[31m Bot FAILED! Respond does not contain input variables. \u001b[0m")
    else:
        print("\u001b[31m Bot FAILED! Got no response. \u001b[0m")
except mechanize._form_controls.ControlNotFoundError:
    print("\u001b[31m Bot FAILED! Got no response. \u001b[0m")
print("---------------------")

# ---------------------------------------------------------
# Bot 2C - Scans for named forms        -------------------
#   Target: color, number, date         -------------------
#   Complexity: simple                  -------------------
# ---------------------------------------------------------
print("Running bot 2C (color, date, number scanner)...")
br.select_form(nr=2)
try:
    br.form['color'] = "#666"
    br.form['date'] = "31-01-1997"
    br.form['number'] = "66"
    res = br.submit()
    if res:
        PrintResponse(res)
        if( ValidadeHack("Chosen options: #666, 31-01-1997, 66", res) ):
            print("\u001b[32m Bot SUCCEEDED! \u001b[0m")
        else:
            print("\u001b[31m Bot FAILED! Respond does not contain input variables. \u001b[0m")
    else:
        print("\u001b[31m Bot FAILED! Got no response. \u001b[0m")
except mechanize._form_controls.ControlNotFoundError:
    print("\u001b[31m Bot FAILED! Got no response. \u001b[0m")
print("---------------------")










# ---------------------------------------------------------
# Bot 3A - Scans for id fields          -------------------
#   Target: input text forms            -------------------
#   Complexity: moderate                -------------------
# ---------------------------------------------------------
print("Running bot 3A (lname, fname scanner)...")
try:
    br.select_form(nr=0)
    controlFName = br.form.find_control(id='fname')
    controlLName = br.form.find_control(id='lname')
    controlFName.value = "HACK1"
    controlLName.value = "HACK2"
    res = br.submit()
    if res:
        PrintResponse(res)
        if( ValidadeHack("Chosen name: HACK1 HACK2", res) ):
            print("\u001b[32m Bot SUCCEEDED! \u001b[0m")
        else:
            print("\u001b[31m Bot FAILED! Respond does not contain input variables. \u001b[0m")
    else:
        print("\u001b[31m Bot FAILED! Got no response. \u001b[0m")
except mechanize._form_controls.ControlNotFoundError:
    print("\u001b[31m Bot FAILED! Got no response. \u001b[0m")
print("---------------------")

# ---------------------------------------------------------
# Bot 3B - Scans for id fields          -------------------
#   Target: radio control               -------------------
#   Complexity: moderate                -------------------
# ---------------------------------------------------------
print("Running bot 3B (pizza scanner)...")
try:
    br.select_form(nr=1)
    controlFName = br.form.find_control(id='pizza')
    controlFName.get("pizza").selected = True
    res = br.submit()
    if res:
        PrintResponse(res)
        if( ValidadeHack("Chosen food: pizza", res) ):
            print("\u001b[32m Bot SUCCEEDED! \u001b[0m")
        else:
            print("\u001b[31m Bot FAILED! Respond does not contain input variables. \u001b[0m")
    else:
        print("\u001b[31m Bot FAILED! Got no response. \u001b[0m")
except mechanize._form_controls.ControlNotFoundError:
    print("\u001b[31m Bot FAILED! Got no response. \u001b[0m")
print("---------------------")

# ---------------------------------------------------------
# Bot 3C - Scans for id fields          -------------------
#   Target: color, number, date         -------------------
#   Complexity: moderate                -------------------
# ---------------------------------------------------------
print("Running bot 3C (color, date, number scanner)...")
try:
    br.select_form(nr=2)
    controlColor = br.form.find_control(id='color')
    controlDate = br.form.find_control(id='date')
    controlNumber = br.form.find_control(id='number')
    controlColor.value = "#666"
    controlDate.value = "31-01-1997"
    controlNumber.value = "66"
    res = br.submit()
    if res:
        PrintResponse(res)
        if( ValidadeHack("Chosen options: #666, 31-01-1997, 66", res) ):
            print("\u001b[32m Bot SUCCEEDED! \u001b[0m")
        else:
            print("\u001b[31m Bot FAILED! Respond does not contain input variables. \u001b[0m")
    else:
        print("\u001b[31m Bot FAILED! Got no response. \u001b[0m")
except mechanize._form_controls.ControlNotFoundError:
    print("\u001b[31m Bot FAILED! Got no response. \u001b[0m")
print("---------------------")
