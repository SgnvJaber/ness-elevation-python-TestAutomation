import time

import allure
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from applitools.common import ScreenOrientation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Test_Mobile_Gestures:
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    expected_time = "09:45"
    expected_menu = "Sample menu"

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

    @allure.title("Verify Swipe")
    @allure.description("This test Verify gestures")
    def test_verify_swipe(self):
        self.move_to_time_section()
        hour_start_location = driver.find_element(By.XPATH, "//*[@contentDescription='12']")
        hour_end_location = driver.find_element(By.XPATH, "//*[@contentDescription='9']")
        driver.swipe(hour_start_location.rect["x"], hour_start_location.rect["y"], hour_end_location.rect["x"],
                     hour_end_location.rect["y"])
        minute_start_location = driver.find_element(By.XPATH, "//*[@contentDescription='15']")
        minute_end_location = driver.find_element(By.XPATH, "//*[@contentDescription='45']")
        driver.swipe(minute_start_location.rect["x"], minute_start_location.rect["y"], minute_end_location.rect["x"],
                     minute_end_location.rect["y"] + (minute_end_location.rect["height"] / 2))
        actual_hour = driver.find_element(By.ID, "hours").text
        actual_minute = driver.find_element(By.ID, "minutes").text
        actual_time = actual_hour + ":" + actual_minute
        assert actual_time == self.expected_time

    @allure.title("Verify Title With Press")
    @allure.description("This test Verify the title inside the menu after long_press")
    def test_verify_title_element(self):
        title_element = self.get_title_element()
        action = TouchAction(driver)
        action.long_press(title_element).release().perform()
        actual_title = driver.find_element(By.XPATH, "//*[@text='Sample menu']").text
        assert actual_title == self.expected_menu

    @allure.step("Navigate to Time")
    def get_title_element(self):
        driver.reset()
        driver.find_element(By.XPATH, "//*[@text='Views']").click()
        driver.find_element(By.XPATH, "//*[@text='Expandable Lists']").click()
        driver.find_element(By.XPATH, "//*[@text='1. Custom Adapter']").click()
        return driver.find_element(By.XPATH, "//*[@text='People Names']")
