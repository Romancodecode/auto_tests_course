from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
123
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    option.add_argument("--disable-gpu")
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=option)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    num_search = browser.find_element(By.ID, 'input_value')
    num = num_search.text
    number = int(num)
    result_sum = calc(number)

    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(result_sum)

    button1 = browser.find_element(By.ID, 'solve')
    button1.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()