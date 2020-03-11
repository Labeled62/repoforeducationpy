from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    y = browser.find_element_by_id("input_value")
    #x = y.get_attribute("valuex")
    x = y.text
    result = calc(x)
    input2 = browser.find_element_by_id("answer")
    input2.send_keys(result)

    #input3 = browser.find_element_by_id("robotCheckbox")
    #input3.click()
    #input3 = browser.find_element_by_id("robotsRule")
    #input3.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    time.sleep(10)
    browser.quit()
