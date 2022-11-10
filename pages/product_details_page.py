from re import X
import time
from pages.driver_utils_page import DriverUtilsPage


class ProductDetailsPage(DriverUtilsPage):

    def __init__(self, driver):
        super().__init__(driver)

    def product_name_loc(self):
        return self.find_element_wait(xpath="//div[@class='aMaAEs']//h1//span")

    def username_loc(self):
        return self.find_element_wait(xpath="//input[@type='password']/../preceding-sibling::div/input")

    def set_username(self, input):
        self.send_keys(self.username_loc(), input)
    
    def password_loc(self):
        return self.find_element(xpath="//input[@type='password']")
    
    def set_password(self, input):
        self.send_keys(self.password_loc(), input)

    def login_btn(self):
        return self.find_element(xpath="//span[text()='Login']/../../button")

    def add_to_cart_loc(self):
        return self.find_element_wait(xpath="//button[text()='ADD TO CART']")

    def wishlist_btn_loc(self, input):
        return self.find_element(xpath="//img[contains(@alt,'"+input+"')]/../../../../following-sibling::div/../div[2]/div")

    def my_account_loc(self):
        return self.find_element_wait(xpath="//div[text()='My Account']")
    
    def my_wishlist_loc(self):
        return self.find_element_wait(xpath="//div[text()='Wishlist']/..")

    def get_product_name(self, input):
        if input in self.product_name_loc().text.strip():
            return True
        return False

    def click_on_add_to_cart_product(self):
        from pages.addtocart_page import AddToCartPage
        if self.wait_for_element(self.add_to_cart_loc()):
            self.click(self.add_to_cart_loc())
            time.sleep(1)
            self.wait_for_page_load()
        return AddToCartPage(self.driver)
    
    def click_on_my_wishlist_in_product(self, input):
        self.wishlist_btn_loc(input).click()
    
    def verfify_login_popup(self):
        return self.is_element_exists(self.username_loc())
    
    def login_to_app(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.login_btn().click()
        time.sleep(2)
    
    def verify_my_account(self):
        return self.is_element_exists(self.my_account_loc())
    
    def click_on_wishlist_in_my_account(self):
        from pages.wishlist_page import WishListPage
        self.hover_on_element(self.my_account_loc())
        self.my_wishlist_loc().click()
        time.sleep(1)
        self.wait_for_page_load()
        return WishListPage(self.driver)


