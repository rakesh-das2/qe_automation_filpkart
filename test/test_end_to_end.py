from test.basetest import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.common_utils import CommonUtils
from utils.excel_utils import XlsxReader
import pytest

class Test_HomePage(BaseTest):

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_verify_homepage_title(self):
        logger = self.getLogger()
        logger.info("Verify flipkart homepage title")
        homepage = HomePage(self.driver)
        logger.info("Launch the app")
        homepage.launch_app_url(CommonUtils.DEFAULT_URL)
        logger.info("Close login popup if display")
        homepage.close_login_popup_if_display()
        data = XlsxReader.get_test_data("test_verify_homepage_title")
        assert self.driver.title == data[0]

    @pytest.mark.parametrize("data", XlsxReader.get_test_data_based_on_sheet("parameterize_data","test_search_function"))
    def test_search_function(self, data):
        logger = self.getLogger()
        logger.info("Verify search function by giving diffrent input")
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
        logger.info("Verify search function by giving diffrent input")
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
        logger.info("Verify product name in PDP page")
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
        search_result_page.find_product_in_search_result_page(data[1]) == True
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
        search_result_page.find_product_in_search_result_page(data[1]) == True
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
        search_result_page.select_4star_ratings()
        logger.info("Verify search " + data[1] + " product should display in search result page")
        search_result_page.find_product_in_search_result_page(data[1]) == True
        logger.info("Click the product " + data[1] + " product should display in search result page")
        product_details_page=search_result_page.click_product_on_search_result_page(data[1])
        logger.info("Verify product should display " + data[1] + " in Product details page")
        assert product_details_page.get_product_name(data[2]) == True
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
        
