from selenium.webdriver.common.by import By
from utils.decorator_utils import DecoratorUtils
import time
from pages.driver_utils_page import DriverUtilsPage


class HomePage(DriverUtilsPage):

    CATEGORY_XPATH="//div[@class='xtXmba']"
    SUB_CATEGORY_XPATH="//div[@class='xtXmba']/../following-sibling::div//div[1]/a"
    ITEM_TYPE_XPATH = "//div[@class='xtXmba']/../following-sibling::div//div[2]/a"
    SUB_SECTION_CSS = "div[class='_2CIhCB']"
    TOP_STORIES_XPATH="//span[text()='Top Stories']"
    by_xpath=By.XPATH


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

    @DecoratorUtils.get_webelement(By.XPATH, TOP_STORIES_XPATH)
    def top_stories_loc(self): pass

    @DecoratorUtils.decorator_func(By.XPATH, CATEGORY_XPATH)
    def category_loc(self):
        breakpoint()
        print("after execution")


    @DecoratorUtils.get_webelements(By.CSS_SELECTOR, SUB_SECTION_CSS)
    def sub_section_loc(self):pass

    @DecoratorUtils.get_webelements(By.XPATH, SUB_CATEGORY_XPATH)
    def sub_category_loc(self):pass

    @DecoratorUtils.get_webelements(By.XPATH, ITEM_TYPE_XPATH)
    def item_type_loc(self):pass

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

    def hover_on_category(self, category_name):
        breakpoint()
        all_category_element=self.category_loc()
        category_flag=False
        for i in all_category_element:
            if category_name in i.text.strip():
                self.hover_on_element(i)
                category_flag= True
                time.sleep(1)
                break
        if category_flag == False:
            print("{} Category not found in list please provide some other category".format(category_name))
    
    def verify_sub_category(self, sub_category_name):
        all_sub_category_element=self.sub_category_loc()
        sub_category_flag=False
        for j in all_sub_category_element:
            if sub_category_name in j.text.strip():
                sub_category_flag=True
                time.sleep(0.5)
                break
        if sub_category_flag == False:
            print("{} sub category not found in list please provide some other sub category".format(sub_category_flag))
        return sub_category_flag

    def hover_on_sub_category(self, sub_category_name):
        all_sub_category_element=self.sub_category_loc()
        for j in all_sub_category_element:
            if sub_category_name in j.text.strip():
                self.hover_on_element(j)
                time.sleep(0.5)
                break
    
    def verify_master_product(self, item_type):
        all_item_loc=self.item_type_loc()
        item_flag=False
        for k in all_item_loc:
            if item_type in k.text.strip():
                item_flag=True
                break
        if item_flag == False:
            print("{} item not found in list please provide some other item".format(item_type))
        return item_flag
    
    def ciick_on_master_item(self,item_type):
        from pages.category_landing_page import CLP
        all_item_loc=self.item_type_loc()
        for k in all_item_loc:
            if item_type in k.text.strip():
                self.js_click(k)
                time.sleep(3)
                #k.click()
                self.wait_for_page_load()
                break
        return CLP(self.driver)
    
    def click_on_sub_section(self, sub_section_name):
        from pages.master_product_page import MasterProductPage
        flag=False
        self.scroll_down()
        self.scroll_till_element(self.top_stories_loc())
        time.sleep(3)
        self.scroll_down()
        self.scroll_till_element(self.top_stories_loc())
        all_sub_section_loc=self.sub_section_loc()
        print(len(all_sub_section_loc))
        for i in all_sub_section_loc:
            if sub_section_name in i.find_element(By.CSS_SELECTOR, "h2").text.strip():
                self.js_click(i.find_element(By.CSS_SELECTOR, "a"))
                flag= True
                time.sleep(2)
                self.wait_for_page_load()
                break
        if flag == False:
            print("{} sub section not found in Homepage".format(sub_section_name))
        return MasterProductPage(self.driver)