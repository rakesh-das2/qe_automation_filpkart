from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils.common_utils import CommonUtils
import time


class BasePage:

    def __init__(self, driver):
        self.driver= driver