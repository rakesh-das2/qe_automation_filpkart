from cmath import log
from selenium.webdriver.support.events import AbstractEventListener
import logging
import datetime
import os
import inspect
from pathlib import Path

class WebDriverEventListner(AbstractEventListener):
    path=os.path.join(os.path.abspath(os.curdir), 'logs')
    log_filename = datetime.datetime.now().strftime("%Y%m%d")
    ROOT_PATH = str(Path(__file__).parent.parent)

    logging.basicConfig(
        #filename=f"{log_filename}.log",
        filename=ROOT_PATH+"/logs/"+'logfile_webdriver.log',
        format="%(asctime)s: %(levelname)s: %(message)s",
        level=logging.INFO
        #fileHandler = logging.FileHandler(ROOT_PATH+"/logs/"+'logfile_webdriver.log')
        

    )

   
    def __init__(self):
        self.logger = logging.getLogger("selenium")
        #loggerName = inspect.stack()[1][3]
        #self.logger = logging.getLogger(loggerName)
        #formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        #fileHandler = logging.FileHandler(self.ROOT_PATH+"/logs/"+'logfile_webdriver.log')
        #fileHandler.setFormatter(formatter)
        #self.logger.addHandler(fileHandler)
        #self.logger.setLevel(logging.INFO)

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