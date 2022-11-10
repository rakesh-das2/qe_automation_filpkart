import time
from pages.driver_utils_page import DriverUtilsPage


class WishListPage(DriverUtilsPage):

    def __init__(self, driver):
        super().__init__(driver)
    
    def delete_icon_loc(self, input):
        return self.find_element_wait(xpath="//div[text()='"+input+"']/../following-sibling::div//img")

    def product_loc(self, input):
        return self.find_element_wait(xpath="//div[text()='"+input+"']")

    def warning_remove_loc(self):
        return self.find_element(xpath="//button[text()='YES, REMOVE']")

    def verify_product(self, input):
        if self.wait_for_element(self.product_loc(input)):
            return self.is_element_exists(self.product_loc(input))
        return False
    
    def remove_product_from_wishlist(self, input):
        self.delete_icon_loc(input).click()
        self.wait_for_element(self.warning_remove_loc())
        self.warning_remove_loc().click()
        time.sleep(1)

    