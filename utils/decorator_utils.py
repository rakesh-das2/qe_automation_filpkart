from utils.common_utils import CommonUtils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class DecoratorUtils:

    def get_webelement(by, locator):
        def decorator_func(func):
            def wrapper(self):
                element=False
                try:
                   element = self.driver.find_element(by, locator)
                except Exception:
                    print("Unable to find element")
                return element
            return wrapper
        return decorator_func

    def get_webelement_wait(by, locator):
        def decorator_func(func):
            def wrapper(self):
                element=False
                try:
                    WebDriverWait(self.driver, CommonUtils.DYNAMIC_WAIT_TIME).until(ec.visibility_of_element_located((by, locator)))
                    element = self.driver.find_element(by, locator)
                except Exception:
                    print("Unable to find element")
                return element
            return wrapper
        return decorator_func

    def decorator_func(by, locator):
        
        def function(func):
            def wrapper(self):
                print(" before %s " % self)
                print(" before %s " % locator)
                element=False
                func(self)
                try:
                    element = self.driver.find_elements(by, locator)
                except Exception:
                    print("Unable to find element ")
                return element
            return wrapper
        return function
        
    def get_webelements_wait(by, locator):
        def decorator_func(func):
            def wrapper(self):
                element=False
                try:
                    WebDriverWait(self.driver, CommonUtils.DYNAMIC_WAIT_TIME).until(ec.visibility_of_element_located((by, locator)))
                    element = self.driver.find_elements(by, locator)
                except Exception:
                    print("Unable to find element")
                return element
            return wrapper
        return decorator_func

    def get_webelements(by, locator):
        def decorator_func(func):
            def wrapper(self):
                element=False
                try:
                    element = self.driver.find_elements(by, locator)
                except Exception:
                    print("Unable to find element")
                return element
            return wrapper
        return decorator_func
 