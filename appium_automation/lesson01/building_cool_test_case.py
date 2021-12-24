import time

import allure
from appium import webdriver
from applitools.common import ScreenOrientation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Test_Building_Cool_Test_Case:
    reportDirectory = 'c:/Automation/Python/test_automation/appium_automation/appium_reports'
    reportFormat = 'xml'
    testName = 'appium.xml'
    dc = {}
    expected_size = 11
    expected_occurrence = 4

    def setup_class(cls):
        global driver
        cls.dc['reportDirectory'] = cls.reportDirectory
        cls.dc['reportFormat'] = cls.reportFormat
        cls.dc['testName'] = cls.testName
        cls.dc['udid'] = 'ce051605b5d4d82c03'
        cls.dc['appPackage'] = 'com.example.android.apis'
        cls.dc['appActivity'] = '.ApiDemos'
        cls.dc['platformName'] = 'android'
        driver = webdriver.Remote('http://localhost:4723/wd/hub', cls.dc)

    def teardown_class(cls):
        driver.quit()

    @allure.title("Verify Activity Title")
    @allure.description("This test Verify Activity Title")
    def test_verify_title(self):
        assert driver.current_activity == ".ApiDemos"

    @allure.title("Verify App Navigation")
    @allure.description("This test Verify App Navigation")
    def test_verify_app_navigation(self):
        #There is a bug with Start Activity line
        driver.start_activity("com.example.ExperiBank", ".LoginActivity");
        time.sleep(1)
        assert driver.find_element(By.XPATH, "//*[@text='login']").text == "Login"
