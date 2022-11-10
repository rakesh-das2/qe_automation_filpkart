from pages.driver_utils_page import DriverUtilsPage
from enum import Flag
from selenium.webdriver.common.by import By
from utils.decorator_utils import DecoratorUtils
import time

class MasterProductPage(DriverUtilsPage):

    LABEL_TITLE_XPATH = "//div[@class='_3vaoUF']/div[1]"
    MASTER_CATLOUGH_XPATH = "//div[@class='_3LU4EM']"
    COUNT_XPATH = "//div[@class='_3vaoUF']/div[2]"
    ABOUT_XPATH = "//div[text()='ABOUT']"  

    def __init__(self, driver):
        super().__init__(driver)

    @DecoratorUtils.get_webelement(By.XPATH, LABEL_TITLE_XPATH)
    def label_title(self):pass
    
    @DecoratorUtils.get_webelements(By.XPATH, MASTER_CATLOUGH_XPATH)
    def master_catalaoug(self):pass

    @DecoratorUtils.get_webelement_wait(By.XPATH, COUNT_XPATH)
    def master_catalaoug_count(self):pass

    @DecoratorUtils.get_webelement_wait(By.XPATH, ABOUT_XPATH)  
    def about_loc(self):pass


    def verify_lable_title(self, label_title_name):
        if label_title_name in self.label_title().text.strip():
            return True
        return False
    
    def scroll_down_until_all_product_display(self):
        data= self.master_catalaoug_count()
        data=data.text.split(" ")
        for i in data:
            if i.isdigit():
                data=int(i)
                break
        master_cataloug=self.master_catalaoug()
        while len(master_cataloug)!=data:
            self.scroll_till_element(self.about_loc())
            time.sleep(2)
            master_cataloug=self.master_catalaoug()

    def get_proudct_row_cell_num(self, product_name):
        flag= False
        master_cataloug=self.master_catalaoug()
        for i in range(len(master_cataloug)):
            if product_name in master_cataloug[i].text.strip():
                total_number=i+1
                cell = (total_number)-((total_number)//4)*4
                print("{} master product name found in {} row and {} cell number".format(product_name, total_number//4 ,4 if cell==0 else cell))
                flag=True
        if flag == False:
            print("{} Master product not found in list".format)
        return flag
