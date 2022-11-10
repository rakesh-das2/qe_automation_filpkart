from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils.common_utils import CommonUtils
import time
from pages.base_page import BasePage

class DriverUtilsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_page_load(self):
        try:
            while True:
                if self.driver.execute_script("return document.readyState") == "complete":
                    break
        except:
            print("Exception occurred !!!!!!!!!!!!!!!!!")
            pass
    
    def is_element_exists(self, element):
        if isinstance(element, str):
            try:
                return self.find_element(xpath=element).is_displayed()
            except:
                print("Element (string) does not exist - Returning False")
                return False
        else:
            return element.is_displayed()

    def click(self, element):
        try:
            time.sleep(1)
            element.click()
        except:
            print("unable to click on button")

    def scroll_down(self,seconds = 0.5):
        try:
            self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") 
            time.sleep(seconds)
        except:
            print("unable to scroll down")

    def scroll_up(self, seconds= 0.5):
        try:
            self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)") 
            time.sleep(seconds)
        except:
            print("unable to scroll up")
    
    def scroll_till_element(self, element, seconds = 0.5 ):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(false);", element)
            time.sleep(seconds)
        except:
            print("unable to scroll till element")

    def wait_for_element(self,element):
        try:
            WebDriverWait(self.driver, CommonUtils.DEFAULT_WAIT_TIME).until(ec.visibility_of(element))
            return True
        except:
            return False

    def send_keys(self, element, data):
        try:
            element.send_keys(data)
        except:
            print("\nelement not found")

    def frame_switch(self, element):
        try:
            self.driver.switch_to.frame(element)
        except:
            print("unable to switch frame")

    def click_with_actions(self, element):
        try:
            ActionChains(self.driver).move_to_element(element).click(on_element=element).perform()
        except:
            print("unable to click element")
            
    def hover_on_element(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(false);", element)
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
        except:
            print("Unable to hover on element")

    def switch_to_child_window(self, open_tabs):
        try:
            WebDriverWait(self.driver, CommonUtils.DEFAULT_WAIT_TIME).until(ec.number_of_windows_to_be(len(open_tabs)+1))
            newWindow = self.driver.window_handles
            value=set(newWindow).difference(open_tabs)
            value=list(value)
            self.driver.delete_all_cookies()
            self.driver.switch_to.window(value[0])
            self.driver.set_window_size(1360, 768)
        except:
            print("Unable to switch child window")
        

    def js_click(self,element):
        try:
            self.driver.execute_script("arguments[0].click();", element)
        except:
            print("js_click function - Unable to find element")

    def find_element_wait(self, xpath=None, css=None, id=None, link_text=None,
                     name=None, tag_name=None, class_name=None, partial_link_text=None):
        try:
            if xpath is not None:
                WebDriverWait(self.driver, CommonUtils.DYNAMIC_WAIT_TIME).until(ec.presence_of_element_located((By.XPATH, xpath)))
                return self.driver.find_element(by=By.XPATH, value=xpath)
            if id is not None:
                WebDriverWait(self.driver, CommonUtils.DYNAMIC_WAIT_TIME).until(ec.visibility_of_element_located((By.ID, id)))
                return self.driver.find_element(by=By.ID, value=id)
            if name is not None:
                WebDriverWait(self.driver, CommonUtils.DYNAMIC_WAIT_TIME).until(ec.visibility_of_element_located((By.NAME, name)))
                return self.driver.find_element(by=By.NAME, value=name)
            if link_text is not None:
                WebDriverWait(self.driver, CommonUtils.DYNAMIC_WAIT_TIME).until(ec.visibility_of_element_located((By.LINK_TEXT, link_text)))
                return self.driver.find_element(by=By.LINK_TEXT, value=link_text)
            if css is not None:
                WebDriverWait(self.driver, CommonUtils.DYNAMIC_WAIT_TIME).until(ec.visibility_of_element_located((By.CSS_SELECTOR, css)))
                return self.driver.find_element(by=By.CSS_SELECTOR, value=css)
            if tag_name is not None:
                WebDriverWait(self.driver, CommonUtils.DYNAMIC_WAIT_TIME).until(ec.visibility_of_element_located((By.TAG_NAME, tag_name)))
                return self.driver.find_element(by=By.TAG_NAME, value=tag_name)
            if class_name is not None:
                WebDriverWait(self.driver, CommonUtils.DYNAMIC_WAIT_TIME).until(ec.visibility_of_element_located((By.CLASS_NAME, class_name)))
                return self.driver.find_element(by=By.CLASS_NAME, value=class_name)
            if partial_link_text is not None:
                WebDriverWait(self.driver, CommonUtils.DYNAMIC_WAIT_TIME).until(ec.visibility_of_element_located((By.PARTIAL_LINK_TEXT,  partial_link_text)))
                return self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value=partial_link_text)
        except:
            print("Unable to find element - %s, %s, %s, %s, %s, %s, %s, %s, %s", xpath, css, id, link_text,
                     name, tag_name, class_name, partial_link_text)
            return False


    def find_element(self, xpath=None, css=None, id=None, link_text=None,
                     name=None, tag_name=None, class_name=None, partial_link_text=None):
        time.sleep(1)
        try:
            if xpath is not None:
                return self.driver.find_element(by=By.XPATH, value=xpath)
            if id is not None:
                return self.driver.find_element(by=By.ID, value=id)
            if name is not None:
                return self.driver.find_element(by=By.NAME, value=name)
            if link_text is not None:
                return self.driver.find_element(by=By.LINK_TEXT, value=link_text)
            if css is not None:
                return self.driver.find_element(by=By.CSS_SELECTOR, value=css)
            if tag_name is not None:
                return self.driver.find_element(by=By.TAG_NAME, value=tag_name)
            if class_name is not None:
                return self.driver.find_element(by=By.CLASS_NAME, value=class_name)
            if partial_link_text is not None:
                return self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value=partial_link_text)
        except:
            print("Unable to find element - %s, %s, %s, %s, %s, %s, %s, %s, %s", xpath, css, id, link_text,
                     name, tag_name, class_name, partial_link_text)
            return False

    def find_elements(self, xpath=None, css=None, id=None, link_text=None,
                     name=None, tag_name=None, class_name=None, partial_link_text=None):
        try:
            if xpath is not None:
                return self.driver.find_elements(by=By.XPATH, value=xpath)
            if id is not None:
                return self.driver.find_elements(by=By.ID, value=id)
            if name is not None:
                return self.driver.find_elements(by=By.NAME, value=name)
            if link_text is not None:
                return self.driver.find_elements(by=By.LINK_TEXT, value=link_text)
            if css is not None:
                return self.driver.find_elements(by=By.CSS_SELECTOR, value=css)
            if tag_name is not None:
                return self.driver.find_elements(by=By.TAG_NAME, value=tag_name)
            if class_name is not None:
                return self.driver.find_elements(by=By.CLASS_NAME, value=class_name)
            if partial_link_text is not None:
                return self.driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=partial_link_text)
        except:
            print("Unable to find element for - %s, %s, %s, %s, %s, %s, %s, %s, %s", xpath, css, id, link_text,
                  name, tag_name, class_name, partial_link_text)
            return False