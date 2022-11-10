from tests.basetest import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.common_utils import CommonUtils
from utils.excel_utils import XlsxReader
import pytest

class Test_E2E(BaseTest):

    @pytest.mark.sanity
    @pytest.mark.regression    
    def test_verify_homepage_title(self):
        from pages.home_page import HomePage
        logger = self.getLogger()
        logger.info("Verify flipkart homepage title")
        homepage = HomePage(self.driver)
        logger.info("Launch the app")
        homepage.launch_app_url(CommonUtils.DEFAULT_URL)
        logger.info("Close login popup if display")
        homepage.close_login_popup_if_display()
        data = XlsxReader.get_test_data("test_verify_homepage_title")
        assert self.driver.title == data[0]

    @pytest.mark.parametrize("data", XlsxReader.get_test_data("test_search_function"))
    def test_search_function(self, data):
        logger = self.getLogger()
        logger.info("Verify search keyword by giving diffrent input")
        homepage = HomePage(self.driver)
        logger.info("Launch the app")
        homepage.launch_app_url(CommonUtils.DEFAULT_URL)
        logger.info("Close login popup if display")
        homepage.close_login_popup_if_display()
        logger.info("Search the product with name " + data + "")
        search_result_page = homepage.enter_value_input_filed(data)
        logger.info("Verify showing result keyword should match")
        assert search_result_page.get_product_in_search_details_page(data) == True

    @pytest.mark.sanity
    def test_search_product_verify_proudct_in_searchresultpage(self):
        logger = self.getLogger()
        logger.info("Search the product and verify product in search result page")
        homepage = HomePage(self.driver)
        logger.info("Launch the app")
        homepage.launch_app_url(CommonUtils.DEFAULT_URL)
        logger.info("Close login popup if display")
        homepage.close_login_popup_if_display()
        data = XlsxReader.get_test_data("test_search_product_verify_proudct_in_searchresultpage")
        logger.info("Search the product with name " + data[0] + "")
        search_result_page = homepage.enter_value_input_filed(data[0])
        logger.info("Verify showing result keyword should match")
        assert search_result_page.get_product_in_search_details_page(data[0]) == True
        logger.info("Verify search " + data[1] + " product should display")
        search_result_page.find_product_in_search_result_page(data[1]) == True

    def test_verify_name_in_pdp_page(self):
        logger = self.getLogger()
        logger.info("Verify product selection should navigate to PDP page")
        homepage = HomePage(self.driver)
        logger.info("Launch the app")
        homepage.launch_app_url(CommonUtils.DEFAULT_URL)
        logger.info("Close login popup if display")
        homepage.close_login_popup_if_display()
        data = XlsxReader.get_test_data("test_verify_name_in_pdp_page")
        logger.info("Search the product with name " + data[0] + "")
        search_result_page = homepage.enter_value_input_filed(data[0])
        logger.info("Verify showing result keyword should match")
        assert search_result_page.get_product_in_search_details_page(data[0]) == True
        logger.info("Verify search " + data[1] + " product should display in search result page")
        assert search_result_page.find_product_in_search_result_page(data[1]) == True
        logger.info("Click the product " + data[1] + " product should display in search result page")
        product_details_page=search_result_page.click_product_on_search_result_page(data[1])
        logger.info("Verify product should display " + data[1] + " in Product details page")
        assert product_details_page.get_product_name(data[1])== True

    def test_verify_add_to_cart_function(self):
        logger = self.getLogger()
        logger.info("Verify user should add and remove product from cart")
        homepage = HomePage(self.driver)
        logger.info("Launch the app")
        homepage.launch_app_url(CommonUtils.DEFAULT_URL)
        logger.info("Close login popup if display")
        homepage.close_login_popup_if_display()
        data = XlsxReader.get_test_data("test_verify_add_to_cart_function")
        logger.info("Search the product with name " + data[0] + "")
        search_result_page = homepage.enter_value_input_filed(data[0])
        logger.info("Verify showing result keyword should match")
        assert search_result_page.get_product_in_search_details_page(data[0]) == True
        logger.info("Verify search " + data[1] + " product should display in search result page")
        assert search_result_page.find_product_in_search_result_page(data[1]) == True
        logger.info("Click the product " + data[1] + " product should display in search result page")
        product_details_page=search_result_page.click_product_on_search_result_page(data[1])
        logger.info("Verify product should display " + data[1] + " in Product details page")
        assert product_details_page.get_product_name(data[1])== True
        logger.info("Click on add to cart button for " + data[1] + " Product in PDP page")
        add_to_cart = product_details_page.click_on_add_to_cart_product()
        logger.info("Verify " + data[1] + " Product should added into cart")
        assert add_to_cart.verify_product_in_cart_page(data[1])== True
        logger.info("Remove " + data[1] + " Product from cart")
        add_to_cart.click_on_remove_btn_for_product(data[1])
        logger.info("Verify " + data[1] + " Product should remove from cart")
        assert add_to_cart.verify_cart_missing()== True

    def test_verify_wishlist_function(self):
        logger = self.getLogger()
        logger.info("Verify user should add and remove product from wishlist")
        homepage = HomePage(self.driver)
        logger.info("Launch the app")
        homepage.launch_app_url(CommonUtils.DEFAULT_URL)
        logger.info("Close login popup if display")
        homepage.close_login_popup_if_display()
        data = XlsxReader.get_test_data("test_verify_wishlist_function")
        logger.info("Search the product with name " + data[0] + "")
        search_result_page = homepage.enter_value_input_filed(data[0])
        logger.info("Verify showing result keyword should match")
        assert search_result_page.get_product_in_search_details_page(data[0]) == True
        logger.info("Verify search " + data[1] + " product should display in search result page")
        assert search_result_page.find_product_in_search_result_page(data[1]) == True
        logger.info("Click the product " + data[1] + " product should display in search result page")
        product_details_page=search_result_page.click_product_on_search_result_page(data[1])
        logger.info("Verify product should display " + data[1] + " in Product details page")
        assert product_details_page.get_product_name(data[1]) == True
        logger.info("Click on wishlist icon for " + data[1] + " Product")
        product_details_page.click_on_my_wishlist_in_product(data[1])
        logger.info("Verify Login popup should display as user not logged in")
        assert product_details_page.verfify_login_popup() == True
        logger.info("Enter Credential and click on login button")
        product_details_page.login_to_app(data[3],data[4])
        logger.info("Verify after my account should dispaly")
        assert product_details_page.verify_my_account() == True
        logger.info("Hover on my account click on wishlist link")
        wishlistpage=product_details_page.click_on_wishlist_in_my_account()        
        logger.info("Verify "+data[1]+" product in wishlist page")
        assert wishlistpage.verify_product(data[1])  == True
        logger.info("Remove "+data[1]+" product from my wishlist")
        wishlistpage.remove_product_from_wishlist(data[1])
        logger.info("Verify "+data[1]+" product should be remove from wishlist")
        assert wishlistpage.verify_product(data[1])  == False

    def test_login(self):
        logger = self.getLogger()
        logger.info("Verify logged in succecs")
        login_page=LoginPage(self.driver)
        logger.info("Launch the app")
        login_page.launch_app_url(CommonUtils.DEFAULT_URL)
        data = XlsxReader.get_test_data("test_login")
        logger.info("Enter valid credential")
        product_details_page=login_page.login_to_app(data[0], data[1])
        logger.info("Verify User should logged in to account")
        assert product_details_page.verify_my_account() == True
        
    def test_verify_category_item(self):
        logger = self.getLogger()
        logger.info("Verify item in Sub Category and Category Page")
        homepage = HomePage(self.driver)
        logger.info("Launch the app")
        homepage.launch_app_url(CommonUtils.DEFAULT_URL)
        logger.info("Close login popup if display")
        homepage.close_login_popup_if_display()
        data = XlsxReader.get_test_data("test_verify_category_item")
        logger.info("Hover on {} category".format(data[0]))
        homepage.hover_on_category(data[0])
        logger.info("Verify {} sub category should display".format(data[1]))
        assert homepage.verify_sub_category(data[1]) == True
        logger.info("Hover on {} sub category".format(data[1]))
        homepage.hover_on_sub_category(data[1])
        logger.info("Verify {} master item should display".format(data[2]))
        assert homepage.verify_master_product(data[2])
        logger.info("Click on {} master item".format(data[2]))
        category_landing_page =homepage.ciick_on_master_item(data[2])              
        logger.info("Verify Page should navigate to CLP page and {} should display".format(data[3]))
        assert category_landing_page.verify_h1_title(data[3]) == True
        logger.info("Verify {}  category should display".format(data[4]))
        assert category_landing_page.verify_main_category(data[4]) == True
        logger.info("Verify {}  category should display".format(data[5]))
        assert category_landing_page.verify_main_category(data[5]) == True

    def test_verify_price_low_to_high_sortby_function(self):
        logger = self.getLogger()
        logger.info("Verify item in Sub Category and Category Page")
        homepage = HomePage(self.driver)
        logger.info("Launch the app")
        homepage.launch_app_url(CommonUtils.DEFAULT_URL)
        logger.info("Close login popup if display")
        homepage.close_login_popup_if_display()
        data = XlsxReader.get_test_data("test_verify_price_low_to_high_sortby_function")
        homepage.hover_on_category(data[0])
        logger.info("Verify {} sub category should display".format(data[1]))
        assert homepage.verify_sub_category(data[1]) == True
        logger.info("Hover on {} sub category".format(data[1]))
        homepage.hover_on_sub_category(data[1])
        logger.info("Verify {} master item should display".format(data[2]))
        assert homepage.verify_master_product(data[2])
        logger.info("Click on {} master item".format(data[2]))
        category_landing_page =homepage.ciick_on_master_item(data[2])              
        logger.info("Verify {} main category should display".format(data[3]))
        assert category_landing_page.verify_main_category(data[3]) == True
        logger.info("Hover on {} category".format(data[3]))
        category_landing_page.hover_on_category(data[3])
        logger.info("Verify {} sub category should display".format(data[4]))
        assert category_landing_page.verify_sub_category_item(data[4]) == True
        logger.info("Click on {} sub category".format(data[4]))
        category_landing_page.click_on_sub_category(data[4])
        logger.info("Verify {} h1 title".format(data[5]))
        assert category_landing_page.verify_h1_title(data[5]) == True
        logger.info("Sort the product by {}".format(data[6]))
        category_landing_page.sort_the_product(data[6])== True
        logger.info("Verify product price display view should be {}".format(data[6]))
        assert category_landing_page.verify_low_to_high_sort_result() == True
                
    def test_verify_master_product(self):
        logger = self.getLogger()
        logger.info("Verify Master product availability")
        homepage = HomePage(self.driver)
        logger.info("Launch the app")
        homepage.launch_app_url(CommonUtils.DEFAULT_URL)
        logger.info("Close login popup if display")
        homepage.close_login_popup_if_display()
        logger.info("Click on sub section")
        data = XlsxReader.get_test_data("test_verify_master_product")
        master_cataloug=homepage.click_on_sub_section(data[0])
        logger.info("Verify lable title should match")
        assert master_cataloug.verify_lable_title(data[0]) == True
        logger.info("Scroll down until all master product display")
        master_cataloug.scroll_down_until_all_product_display()
        logger.info("Verify {} master product should display and print row and cell number")
        assert master_cataloug.get_proudct_row_cell_num(data[1]) == True
        