from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from utils.decorator_utils import DecoratorUtils
from pages.driver_utils_page import DriverUtilsPage
import time

class LoginPage(DriverUtilsPage):

    USERNAME_XPATH = "//input[@type='password']/../preceding-sibling::div/input"
    PASSWORD_XPATH = "//input[@type='password']"
    SUBMIT_BUTTON_XPATH ="//span[text()='Login']/../../button"

    def __init__(self, driver):
        super().__init__(driver)

    @DecoratorUtils.get_webelement(By.XPATH, USERNAME_XPATH)
    def username_element(self):pass        
    
    @DecoratorUtils.get_webelement(By.XPATH, PASSWORD_XPATH)
    def password_element(self):pass
    
    @DecoratorUtils.get_webelement(By.XPATH, SUBMIT_BUTTON_XPATH)
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
