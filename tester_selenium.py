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


def was_successful(formId = 0):
    result = driver.find_element_by_name("result1")
    if(formId == 1):
        result = driver.find_element_by_name("result2")
    elif(formId == 2):
        result = driver.find_element_by_name("result3")
    innerHTML = result.get_attribute('innerHTML')
    if "HaCkEd" in innerHTML:
        print("Got result: " + ConsoleColors.YELLOW + innerHTML + ConsoleColors.RESET)
        return True
    return False


try:
    fname = driver.find_element_by_id("fname")
    fname.send_keys("HaCkEd")
    driver.find_element_by_id("submit").click()
    if was_successful(0):
        print(ConsoleColors.GREEN + "\tBot SUCCEEDED!" + ConsoleColors.RESET)
    else:
        print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Respond does not contain input variables.")
except selenium.common.exceptions.NoSuchElementException:
    print(ConsoleColors.RED + "\tBot FAILED! " + ConsoleColors.RESET + "Could not find element.")
