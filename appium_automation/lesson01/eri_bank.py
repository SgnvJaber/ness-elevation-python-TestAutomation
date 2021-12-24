from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Test_Building_Test_Case():
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'

    def setup_class(cls):
        global driver
        cls.dc['reportDirectory'] = cls.reportDirectory
        cls.dc['reportFormat'] = cls.reportFormat
        cls.dc['testName'] = cls.testName
        cls.dc['udid'] = 'ce051605b5d4d82c03'
        cls.dc['appPackage'] = 'com.experitest.ExperiBank'
        cls.dc['appActivity'] = '.LoginActivity'
        cls.dc['platformName'] = 'android'
        driver = webdriver.Remote('http://localhost:4723/wd/hub', cls.dc)

    def teardown_class(cls):
        driver.quit()

    def test_01(self):
        driver.find_element(By.XPATH, "//*[@id='usernameTextField']").send_keys("company")
        driver.find_element(By.XPATH, "//*[@id='passwordTextField']").send_keys("company")
        driver.find_element(By.XPATH, "//*[@text='Login']").click()
        driver.find_element(By.XPATH, "//*[@text='Logout']").click()
