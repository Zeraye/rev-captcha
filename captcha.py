from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://revcaptcha.com/')
driver.implicitly_wait(20)

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


time.sleep(1)


######## PIERWSZA WERSJA WOLNA ROBI OKOŁO 95 ########

# i = 0
# divs = driver.find_elements_by_class_name('revCaptchaEquationRow')
# for div in divs:
#     equation = div.get_attribute('innerHTML')
#     equation = equation[7:].split('<')[0]
#     answer = solve(equation)
#     input_label = div.find_element_by_name('solution-'+str(i))
#     i += 1
#     print(i)
#     pyperclip.copy(answer)
#     input_label.send_keys(Keys.CONTROL,'v')


######## JS SIĘ ZWALIŁO I COFA INPUT VALUE ########
######## JS CAŁY CZAS ZWALONY ALE SZYBKOŚĆ JEST TURBO MOCNA WIĘC DZIAŁA ########

input = ""

for i in range(500):
    input += f"""document.querySelector("input[name='solution-{i}']").value = eval(document.querySelectorAll("div[class='revCaptchaEquationRow'] label")[{i}].textContent);"""


driver.execute_script(input)

submit_btn = driver.find_element_by_class_name('revCaptchaSubmitButton')
submit_btn.click()

######## DZIAŁA ALE WOLNO OKOŁO 90 ROBI ########

# inputs = driver.find_elements_by_tag_name('input')[:-1]
# equations = driver.find_elements_by_class_name('revCaptchaEquationRow')

# i = 0

# for i in range(len(inputs)):
#     equation = equations[i].text
#     answer = solve(equation)
#     pyperclip.copy(answer)
#     inputs[i].send_keys(Keys.CONTROL,'v')
#     print(i)
    
