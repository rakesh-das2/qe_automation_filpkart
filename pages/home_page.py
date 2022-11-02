from re import X
from pages.webdriver_utils import WebDriverUtils

class HomePage(WebDriverUtils):

    def __init__(self, driver):
        super().__init__(driver)

    
    def search_input_loc(self):
        return self.find_element(name="q")

    def set_input(self, input):
        self.send_keys(self.search_input_loc(), input)

    def click_submit_btn_loc(self):
        return self.find_element(css="button[type='submit']")

    def login_popup_close_loc(self):
        return self.find_element_wait(xpath="//button[text()='✕']")

    def launch_app_url(self, url):
        self.driver.delete_all_cookies()
        self.driver.get(url)

    def close_login_popup_if_display(self):
        element=self.login_popup_close_loc()
        if element!=False:
            element.click()
    
    
    def enter_value_input_filed(self, input):
        from pages.search_result_page import SearchResultPage
        self.set_input(input)
        self.click_submit_btn_loc().click()
        return SearchResultPage(self.driver)
    
