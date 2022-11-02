from xml.dom.minidom import Element
from pages.webdriver_utils import WebDriverUtils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils.common_utils import CommonUtils
from selenium.webdriver.support.wait import WebDriverWait

import time

class LoginPage(WebDriverUtils):

    USERNAME_XPATH = "//input[@type='password']/../preceding-sibling::div/input"
    PASSWORD_XPATH = "//input[@type='password']"
    SUBMIT_BUTTON_XPATH ="//span[text()='Login']/../../button"

    def __init__(self, driver):
        super().__init__(driver)

    def get_webelement(by, locator):
        def decorator_func(func):
            def wrapper(self):
                element=False
                try:
                   element = self.driver.find_element(by, locator)
                except Exception:
                    print("Unable to find element because")
                return element
            return wrapper
        return decorator_func

    @get_webelement(By.XPATH, USERNAME_XPATH)
    def username_element(self):pass
    
    @get_webelement(By.XPATH, PASSWORD_XPATH)
    def password_element(self):pass
    
    @get_webelement(By.XPATH, SUBMIT_BUTTON_XPATH)
    def submit_button_element(self):pass

    def login_to_app(self, username, password):
        from pages.product_details_page import ProductDetailsPage
        self.send_keys(self.username_element(), username)
        self.send_keys(self.password_element(), password)
        self.submit_button_element().click()
        time.sleep(2)
        return ProductDetailsPage(self.driver)

    def launch_app_url(self, url):
        self.driver.delete_all_cookies()
        self.driver.get(url)

