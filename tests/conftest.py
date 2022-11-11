from utils.common_utils import CommonUtils
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.support.events import EventFiringWebDriver
from helpers.webdriver_event_listner import WebDriverEventListner
web_driver = None


@pytest.fixture()
def setup(request, browser, delete_file):
    global web_driver
    data=CommonUtils.read_json_file("./capabilities.json")
    web_driver=None
    if web_driver is None and browser=='chrome':
        chrome_options = Options()
        chrome_options.add_argument(data['disable-infobars'])
        chrome_options.add_argument(data['disable-notification'])
        chrome_options.add_experimental_option(
        "excludeSwitches", data['excludeSwitches'])
        chrome_options.add_argument(data['ignore_certtificate_error'])
        chrome_options.add_argument(data['disable-dev-shm-usage'])
        chrome_options.add_argument(data['dns-prefetch-disable'])
        chrome_options.add_argument(data['disable-gpu'])
        if CommonUtils.HEADLESS:
            chrome_options.add_argument(data['headless'])
        print("################################")
        browser_path=os.path.join(os.path.abspath(os.curdir), 
            'resources','win_chromedriver.exe')
        web_driver = webdriver.Chrome(service=Service(
                executable_path=browser_path), options=chrome_options)
    web_driver.set_window_size(1360, 768)
    #web_driver = EventFiringWebDriver(web_driver, EventListeners())
    web_driver=EventFiringWebDriver(web_driver, WebDriverEventListner())
    request.cls.driver = web_driver
    yield
    web_driver.quit()

@pytest.fixture(scope="session")
def delete_file():
    logs_path=os.path.join(os.path.abspath(os.curdir), 
    'logs')
    report_path=os.path.join(os.path.abspath(os.curdir), 
    'html_report')
    CommonUtils.delete_all_content_from_directory(logs_path)
    CommonUtils.delete_all_content_from_directory(report_path)


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption('-B')

def pytest_addoption(parser):
    parser.addoption("-B", "--browser",
                     dest="browser",
                     action="store",
                     default='chrome',
                     help="Browser. Valid options is chrome")

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_").replace("test/", "")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    if web_driver !=None:  
        web_driver.get_screenshot_as_file(os.path.join(os.path.abspath(os.curdir), 'html_report',name))