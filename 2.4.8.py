from selenium import webdriver
import time
import math
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    element = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"100"))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    y = browser.find_element_by_id("input_value")
    # x = y.get_attribute("valuex")
    x = y.text
    result = calc(x)
    input2 = browser.find_element_by_id("answer")
    input2.send_keys(result)
    button = browser.find_element_by_id("solve")
    button.click()



    #xet = x.text
    #result = calc(x)
    #input2 = browser.find_element_by_id("answer")
    #input2.send_keys(result)
    #current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    #file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    #element = browser.find_element_by_name("file")
    #element.send_keys(file_path)
    #input3 = browser.find_element_by_id("robotCheckbox")
    #input3.click()
    #input3 = browser.find_element_by_id("robotsRule")
    #input3.click()

    # Отправляем заполненную форму


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    time.sleep(10)
    browser.quit()
