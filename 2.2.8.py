from selenium import webdriver
import time
import math
import os

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    inputfn = browser.find_element_by_name("firstname")
    inputfn.send_keys("First Name")
    inputln = browser.find_element_by_name("lastname")
    inputln.send_keys("Last Name")
    inputen = browser.find_element_by_name("email")
    inputen.send_keys("test@testoos.ru")

    #xet = x.text
    #result = calc(x)
    #input2 = browser.find_element_by_id("answer")
    #input2.send_keys(result)
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element = browser.find_element_by_name("file")
    element.send_keys(file_path)
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
