from re import X
import time
from pages.driver_utils_page import DriverUtilsPage



class SearchResultPage(DriverUtilsPage):

    def __init__(self, driver):
        super().__init__(driver)

    def showing_result_count_loc(self):
        self.wait_for_page_load()
        return self.find_element_wait(xpath="//span[contains(text(), 'Showing')]")

    def product_loc(self, input):
        return self.find_elements(xpath="//a[@title='"+input+"']")

    def all_product_loc(self):
        return self.find_elements(xpath="//a[@target='_blank' and @title]")

    def next_button_loc(self):
        return self.find_element(xpath="//span[text()='Next']/..")

    def flter_4star_loc(self):
        return self.find_element(xpath="//div[text()='4★ & above']/preceding-sibling::div")
    
    def get_product_in_search_details_page(self, data):
        if data in self.showing_result_count_loc().text.strip():
            return True
        return False

    def select_4star_ratings(self):
        self.flter_4star_loc().click()

    def find_product_in_search_result_page(self, data):
        eariler_product_name=None
        product_name=None
        value = len(self.product_loc(data))
        while value == 0:
            if self.wait_for_element(self.next_button_loc()):
                time.sleep(1)
                product_list=self.all_product_loc()
                product_name=product_list[0].text.strip()
                if(product_name!=eariler_product_name):
                    eariler_product_name=product_name
                else:
                    break
                self.js_click(self.next_button_loc())
            else:
                break
            time.sleep(1)
            list=self.product_loc(data)
            value = len(list)
            time.sleep(1)
        if value <= 1:
            return True
        else:
            return False

    def click_product_on_search_result_page(self, input):
        from pages.product_details_page import ProductDetailsPage
        product_list=self.product_loc(input)
        opened_tabs=self.driver.window_handles
        product_list[0].click()
        self.switch_to_child_window(opened_tabs)
        return ProductDetailsPage(self.driver)