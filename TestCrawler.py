import mechanize
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
br = mechanize.Browser()
br.set_handle_robots(False)
br.open("https://localhost:44307/")



# Dedicated scanner personalized for our website
print("---------------------")
print("Running advanced bot...")
formNames = []
for form in br.forms():
    for control in form.controls:
        formNames.append(control.name)
br.select_form(nr=0)
br.form[formNames[0]] = 'HACK1'
br.form[formNames[1]] = 'HACK2'
req = br.submit()
if req:
    print("Bot SUCCEEDED!")
    print("Got response: \u001b[32m")
    for r in req:
        print(r)
    print("\u001b[0m")





# Simple scanner for fname and lname
print("---------------------")
print("Running simple bot...")
br.select_form(nr=0)
try:
    br.form['fname'] = 'HACK1'
    br.form['lname'] = 'HACK2'
    req = br.submit()
    if req:
        print("Got response: \u001b[32m")
        for r in req:
            print(r)
        print("\u001b[0m")
except mechanize._form_controls.ControlNotFoundError:
    print("Bot FAILED!")
print("---------------------")
