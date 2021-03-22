# importing libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
from selenium.webdriver.common.keys import Keys
import time

# driver options
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://revcaptcha.com/')
driver.implicitly_wait(20)

# clicking first checkbox
checkbox_btn = driver.find_element_by_class_name('revCaptchaCheckbox')
checkbox_btn.click()

def solve(equation):
    lst = [equation[i] for i in range(len(equation))]

    for item in lst:
        if item == '+':
            new_equation = equation.split(item)
            return int(new_equation[0]) + int(new_equation[1])
        elif item == '-':
            new_equation = equation.split(item)
            return int(new_equation[0]) - int(new_equation[1])
        elif item == '*':
            new_equation = equation.split(item)
            return int(new_equation[0]) * int(new_equation[1])
    return ''

# wait to load animation
time.sleep(1)

input = ''

# not best, but work okay?
for i in range(500):
    input += f"""document.querySelector("input[name='solution-{i}']").value = eval(document.querySelectorAll("div[class='revCaptchaEquationRow'] label")[{i}].textContent);"""


driver.execute_script(input)

# clicking last button
submit_btn = driver.find_element_by_class_name('revCaptchaSubmitButton')
submit_btn.click()
