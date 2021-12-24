import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import xml.etree.ElementTree as ET


@pytest.fixture(scope='class')
def init_driver(request):
    if get_data("Browser") == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif get_data("Browser") == "edge":
        srv = Service(EdgeChromiumDriverManager().install())
        driver = selenium.webdriver.Edge(service=srv)
    elif get_data("Browser") == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        driver = None
        print("Wrong input, unrecognized browser")
    driver.maximize_window()
    driver.implicitly_wait(1)
    request.cls.driver = driver
    yield
    driver.quit()


def get_data(node_name):
    root = ET.parse(
        'C:/Automation/Python/test_automation/selenium_automation/lesson05/pytest_advanced_demo/configuration.xml').getroot()
    return root.find(".//" + node_name).text
