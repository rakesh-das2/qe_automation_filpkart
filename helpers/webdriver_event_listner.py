from cmath import log
from selenium.webdriver.support.events import AbstractEventListener
import logging
import datetime
import os
class WebDriverEventListner(AbstractEventListener):
    path=os.path.join(os.path.abspath(os.curdir), 'logs')
    log_filename = datetime.datetime.now().strftime("%Y%m%d")
   
    logging.basicConfig(
        filename=f"{log_filename}.log",
        format="%(asctime)s: %(levelname)s: %(message)s",
        level=logging.INFO
    )
    def __init__(self):
        self.logger = logging.getLogger("selenium")

    def before_navigate_to(self, url, driver):
        self.logger.info(f"Navigating to {url}")
        print(f"Navigating to {url}")

    def after_navigate_to(self, url, driver):
        self.logger.info(f"{url} opened")
        print(f"{url} opened")

    def before_find(self, by, value, driver):
        self.logger.info(f"Searching for element by {by} {value}")
        print(f"Searching for element by {by} {value}")

    def after_find(self, by, value, driver):
        self.logger.info(f"Element by {by} {value} found")
        print(f"Element by {by} {value} found")

    def before_click(self, element, driver):
        self.logger.info("Clicking on {}".format(element))
        print("Clicking on {}".format(element))
        
    def after_click(self, element, driver):
        self.logger.info("{} clicked".format(element))
        print("{} clicked".format(element))

    def before_change_value_of(self, element, driver):
        self.logger.info(f"{element.get_attribute('text')} value changed")

    def before_quit(self, driver):
        self.logger.info("Driver quitting")

    def after_quit(self, driver):
        self.logger.info("Driver quitted")

    def on_exception(self, exception, driver):
        self.logger.info(exception)