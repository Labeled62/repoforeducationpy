from selenium import webdriver
import time
import unittest
welc = "Congratulations! You have successfully registered!"
def reg(link):
      link = "http://suninjuly.github.io/registration1.html"
      browser = webdriver.Chrome()
      browser.get(link)

      input1 = browser.find_element_by_xpath("//div[@class='first_block']//div[@class='form-group first_class']//input[@class='form-control first']")
      input1.send_keys("Ivan")

      input2 = browser.find_element_by_xpath("//div[@class='first_block']//div[@class='form-group second_class']//input[@class='form-control second']")
      input2.send_keys("Petrov")

      input3 = browser.find_element_by_xpath("//div[@class='first_block']//div[@class='form-group third_class']//input[@class='form-control third']")
      input3.send_keys("testoos@in.ru")


      # Отправляем заполненную форму
      button = browser.find_element_by_css_selector("button.btn")
      button.click()

      # Проверяем, что смогли зарегистрироваться
      welcome_text_elt = browser.find_element_by_tag_name("h1")
      welcome_text = welcome_text_elt.text
      return welcome_text



class TestsForPages(unittest.TestCase):
   def test_first_page(self):
      p1 = reg("http://suninjuly.github.io/registration1.html")
      self.assertEqual(p1, welc)

   def test_second_page(self):
      p2 = reg("http://suninjuly.github.io/registration2.html")
      self.assertEqual(p2, welc)


if __name__ == "__main__":
   unittest.main()

