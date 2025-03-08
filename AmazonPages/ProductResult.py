from selenium.webdriver.common.by import By

class IphonePage:


     def __init__(self,driver):
         self.driver = driver
         self.product_search_result = (By.CSS_SELECTOR,"h2[class='a-size-base a-spacing-small a-spacing-top-small a-text-normal']")
         self.gaming_laptop = (By.CSS_SELECTOR, "div>img[src='https://m.media-amazon.com/images/I/71ShAbeIRdL._AC_UY218_.jpg']")



     def get_product_search_result(self):
         return self.driver.find_element(*self.product_search_result)

     def get_product_result_search_text(self):
         return self.driver.find_element(*self.product_search_result).text

     def click_product(self):
         self.driver.execute_script("window.scrollBy(0,200)")
         self.driver.find_element(*self.gaming_laptop).click()
