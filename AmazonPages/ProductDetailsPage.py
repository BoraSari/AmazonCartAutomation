from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class DetailsPage:


      def __init__(self,driver):
          self.driver = driver
          self.memory_change = (By.XPATH,"(//span/input[@name='1'])[3]")
          self.discount_price = (By.CSS_SELECTOR,"td>span[class='a-color-price']")
          self.add_to_cart_button = (By.ID,"add-to-cart-button")
          self.no_thanks_section = (By.CSS_SELECTOR,"input[aria-labelledby='attachSiNoCoverage-announce']")
          self.go_to_cart_section = (By.CSS_SELECTOR,"span>a[href='/cart?ref_=sw_gtc']")


      def get_memory_section(self):
       return  self.driver.find_element(*self.memory_change)


      def click_memory_section(self):
        self.driver.find_element(*self.memory_change).click()


      def get_calculated_discount(self):
        return self.driver.find_element(*self.discount_price)


      def get_calculated_discount_text(self):
        return self.driver.find_element(*self.discount_price).text


      def add_product_in_cart(self):
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(self.add_to_cart_button))
        self.driver.find_element(*self.add_to_cart_button).click()


      def click_no_thanks_section(self):
         WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(self.no_thanks_section))
         self.driver.find_element(*self.no_thanks_section).click()


      def navigate_cart_details_page(self):
         WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.go_to_cart_section))
         self.driver.find_element(*self.go_to_cart_section).click()










