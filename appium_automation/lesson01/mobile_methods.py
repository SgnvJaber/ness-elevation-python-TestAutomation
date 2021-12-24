import time

import allure
from appium import webdriver
from applitools.common import ScreenOrientation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Test_Mobile_Methods:
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
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

    @allure.title("Verify List Size")
    @allure.description("This test Verify that list size is as expected")
    def test_verify_list_size(self):
        list = driver.find_elements(By.XPATH, "//*[@id='list']/android.widget.TextView")
        self.print_content_rect()
        self.print_activity_details()
        assert len(list) == self.expected_size

    @allure.title("Verify ExperiBank App is installed")
    @allure.description("This test Verify that ExperiBank is installed")
    def test_verify_eri_is_installed(self):
        assert driver.is_app_installed("com.experitest.ExperiBank")

    @allure.title("Verify Orientation")
    @allure.description("This test Verify screen orientation")
    def test_verify_orientation(self):
        try:
            assert driver.orientation == ScreenOrientation.LANDSCAPE
        except AssertionError as e:
            driver.orientation = "LANDSCAPE"
            time.sleep(1)
            driver.orientation = "PORTRAIT"

    @allure.title("Verify Screenshot")
    @allure.description("This test Verify screenshot ")
    def test_verify_screenshot(self):
        driver.open_notifications()
        time.sleep(1)
        driver.save_screenshot("notification.png")
        driver.press_keycode(3)  # Go Back
        driver.save_screenshot("home.png")

    @allure.title("Verify Locker")
    @allure.description("This test Verify the device locker")
    def test_verify_locker(self):
        if not driver.is_locked():
            driver.lock()
        time.sleep(1)
        if driver.is_locked():
            driver.unlock()
        time.sleep(1)
        assert not driver.is_locked()

    @allure.title("Verify List View Count")
    @allure.description("This test Verify the list View Count")
    def test_verify_list_view_count(self):
        source = driver.page_source
        assert source.count("ListView") == self.expected_occurrence

    @allure.step("Print TextView Rect")
    def print_content_rect(self):
        content = driver.find_element(By.XPATH, "//*[@contentDescription='Content']")
        print("width: " + str(content.rect["width"]) + " Height: " + str(content.rect["height"]))
        print("X: " + str(content.rect["x"]) + " Y:" + str(content.rect["y"]))

    @allure.step("Print Activity Details")
    def print_activity_details(self):
        print(("Activity: " + driver.current_activity))
        print("Time: " + driver.device_time)
