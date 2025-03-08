import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class CartDetails:


     def __init__(self,driver):
         self.driver = driver
         self.add_button = (By.XPATH,"//button/*[@class='a-icon a-icon-small-add']")
         self.new_product_price = (By.ID,"sc-subtotal-amount-activecart")
         self.delete_button = (By.CSS_SELECTOR,"input[name^='submit.delete'][value='Delete']")
         self.delete_message = (By.XPATH, "//div[@data-action='delete'][1]")



     def increase_total_product_in_basket(self):
            WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(self.add_button))
            for i in  range(2):
             time.sleep(3)
             self.driver.find_element(*self.add_button).click()





     def get_new_product_price(self):
         WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(self.new_product_price))
         return self.driver.find_element(*self.new_product_price)



     def get_new_product_price_text(self):
         return self.driver.find_element(*self.new_product_price).text



     def delete_product_on_cart_page(self):
         WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.delete_button))
         time.sleep(10)
         self.driver.find_element(*self.delete_button).click()


     def get__product_delete_text(self):
         WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(self.delete_button))
         return self.driver.find_element(*self.delete_message).text







