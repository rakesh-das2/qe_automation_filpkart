from pages.webdriver_utils import WebDriverUtils
import time


class AddToCartPage(WebDriverUtils):

    def __init__(self, driver):
        super().__init__(driver)

    def missing_cart_items(self):
        return self.find_element_wait(xpath="//div[text()='Missing Cart items?']")

    def product_name_loc(self, input):
        self.wait_for_page_load()
        return self.find_element_wait(xpath="//a[contains(text(),'"+input+"')]")

    def remove_product_from_cart_loc(self, input):
        return self.find_element(xpath="//a[contains(text(),'"+input+"')]/../../../following-sibling::div//div[text()='Remove']")

    def remove_btn_on_popup_loc(self):
        return self.find_element_wait(xpath="//div[text()='Remove Item']/following-sibling::div//div[text()='Remove']")

    def verify_product_in_cart_page(self, input):
        if input in self.product_name_loc(input).text.strip():
            return True
        return False

    def click_on_remove_btn_for_product(self, input):
        self.scroll_down()
        if self.wait_for_element(self.remove_product_from_cart_loc(input)):
            self.remove_product_from_cart_loc(input).click()
            if self.wait_for_element(self.remove_btn_on_popup_loc()):
                self.click(self.remove_btn_on_popup_loc())
                time.sleep(1)
                self.wait_for_page_load()

    def verify_cart_missing(self):
        return self.is_element_exists(self.missing_cart_items())