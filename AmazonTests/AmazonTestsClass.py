import pytest
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from AmazonPages.DATAS import base_url,product,total_result_text,discount_percent,product_price_on_card_Page,delete_message_after_product_deletion
from AmazonPages.AmazonMainPage import  MainPage
from AmazonPages.ProductResult import IphonePage
from AmazonPages.ProductDetailsPage import DetailsPage
from AmazonPages.CartDetailsPage import CartDetails

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()


def test_for_product_search_result(driver):
    #Class
    main_page = MainPage(driver)
    result_page = IphonePage(driver)
    main_page.search_product(product)

   #Functions
    product_result_message = result_page.get_product_search_result()
    product_result_message_text = result_page.get_product_result_search_text()
    expected_result_message_text = total_result_text

    assert product_result_message.is_displayed(),f"{product_result_message} can display on web application"
    assert  expected_result_message_text in product_result_message_text,f"{expected_result_message_text} contains {product_result_message_text}"


def test_product_discount(driver):
    #Class
    main_page = MainPage(driver)
    result_page = IphonePage(driver)
    product_details_page = DetailsPage(driver)

    #Functions
    main_page.search_product(product)
    result_page.click_product()
    product_details_page.click_memory_section()

    memory_option = product_details_page.get_memory_section()
    assert memory_option.is_displayed(), f"{memory_option} can display on web application"

    discounted_price = product_details_page.get_calculated_discount()
    discounted_price_text = product_details_page.get_calculated_discount_text()
    expected_price_text = discount_percent

    assert discounted_price.is_displayed(),f"{discounted_price} can display on application"
    assert expected_price_text in discounted_price_text,f"{expected_price_text} contains {discounted_price_text}"



def test_product_price_on_card_page(driver):
    #Class
    main_page = MainPage(driver)
    result_page = IphonePage(driver)
    product_details_page = DetailsPage(driver)
    cart_details_page = CartDetails(driver)

    #Functions
    main_page.search_product(product)
    result_page.click_product()
    product_details_page.add_product_in_cart()
    product_details_page.click_no_thanks_section()
    product_details_page.navigate_cart_details_page()
    cart_details_page.increase_total_product_in_basket()

    calculated_price_text =cart_details_page.get_new_product_price_text()
    print("PRODUCT PRİCE = ",calculated_price_text)
    expected_new_price_text = product_price_on_card_Page
    assert expected_new_price_text==calculated_price_text,f"{expected_new_price_text} equals {calculated_price_text} on web application"




def test_product_removed_on_card_page_test(driver):
    # Class
    main_page = MainPage(driver)
    result_page = IphonePage(driver)
    product_details_page = DetailsPage(driver)
    cart_details_page = CartDetails(driver)

    #Functions
    main_page.search_product(product)
    result_page.click_product()
    product_details_page.add_product_in_cart()
    product_details_page.click_no_thanks_section()
    product_details_page.navigate_cart_details_page()
    cart_details_page.increase_total_product_in_basket()
    cart_details_page.delete_product_on_cart_page()

    delete_text = cart_details_page.get__product_delete_text()
    print("Delete text=", delete_text)
    expected_delete_text= delete_message_after_product_deletion
    assert expected_delete_text == delete_text, f"{expected_delete_text} equals {delete_text}"









