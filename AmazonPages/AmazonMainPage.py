from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class MainPage:


     def __init__(self,driver):
         self.driver = driver
         self.search_box_field = (By.ID,"twotabsearchtextbox")




     def search_product(self,product):
         self.driver.find_element(*self.search_box_field).send_keys(product,Keys.ENTER)


