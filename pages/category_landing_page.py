from pages.driver_utils_page import DriverUtilsPage
from selenium.webdriver.common.by import By
from utils.decorator_utils import DecoratorUtils
import time

class CLP(DriverUtilsPage):

    ITEM_XPATH ="//span[contains(text(), 'Showing')]/preceding-sibling::h1"
    MAIN_CATEGORY_ITEM_XPATH="//div[@id='container']/div/div[2]//div[1]/span"
    SUB_CATEGORY_XPATH="//div[@class='_1fwVde']/a"
    SORT_BY_XPATH="//h1/following-sibling::div/div"
    PRICE_XPATH= "//div[@class='_30jeq3 _1_WHN1']"
    
    def __init__(self, driver):
        super().__init__(driver)

    @DecoratorUtils.get_webelement_wait(By.XPATH, ITEM_XPATH)
    def category_item_loc(self):pass
    
    @DecoratorUtils.get_webelements_wait(By.XPATH, MAIN_CATEGORY_ITEM_XPATH)
    def main_category_loc(self):pass
    
    @DecoratorUtils.get_webelements_wait(By.XPATH, SUB_CATEGORY_XPATH)
    def sub_category_loc(self):pass
    
    @DecoratorUtils.get_webelements_wait(By.XPATH, SORT_BY_XPATH)
    def sort_by_loc(self):pass
    
    @DecoratorUtils.get_webelements_wait(By.XPATH, PRICE_XPATH)
    def price_loc(self):pass
    
    def hover_on_category(self,category_name):
        category_flag=False
        for i in self.main_category_loc():
            if category_name in i.text.strip():
                self.hover_on_element(i)
                category_flag =True
                break
            if category_flag == False:
                print("{} category name not found please provide avvalible category name".format(category_name))

    def verify_sub_category_item(self, sub_category):
        sub_category_flag= False
        all_sub_category=self.sub_category_loc()
        for j in all_sub_category:
            if sub_category in j.text.strip():
                sub_category_flag=True
                break
        return sub_category_flag

    def click_on_sub_category(self, item_name):
        all_sub_category=self.sub_category_loc()
        for j in all_sub_category:
            if item_name in j.text.strip():
                j.click()
                time.sleep(2)
                self.wait_for_page_load()
                break
                
    def sort_the_product(self, sort_type):
        sort_type_flag=False
        for i in self.sort_by_loc():
            for i in self.sort_by_loc():
                if sort_type in i.text.strip():
                    sort_type_flag= True
                    i.click()
                    time.sleep(1)
                    self.wait_for_page_load()
            if sort_type_flag == False:
                print("{} sort type not found".format(sort_type))
            
    def verify_low_to_high_sort_result(self):
        price_flag=None
        for j in self.price_loc():
            price=j.text.strip().replace("₹", "").replace(",","")
            price=int(price)
            print(price)
            previous=0
            if previous<=price:
                previous=price
                price_flag=True
            else:
                price_flag=False
                break
        if price_flag == False:
                    print("Price not matched with low to high sorting type")
        return price_flag
                                

    def verify_h1_title(self, item_type):
        if item_type in self.category_item_loc().text.strip():
            return True 
        else:
            print("{} item not found please provide correct item name".format(item_type))
        return False

    def verify_main_category(self, category_name):
        flag = False
        for i in self.main_category_loc():
            if category_name in i.text.strip():
                flag =True
                break
        if flag == False:
            print("{} category not found please provide correct category name".format(category_name))
        
        return flag