from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium_automation.lesson03.webdriver_event_listener import EventListener


class TestListenerReport:
    def setup_class(cls):
        global driver
        edriver = webdriver.Chrome(ChromeDriverManager().install())
        driver = EventFiringWebDriver(edriver, EventListener())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        driver.implicitly_wait(2)

    def teardown_class(cls):
        driver.quit()

    def test_1(self):
        driver.find_element_by_id("user-name").send_keys("standard_user")
        driver.find_element_by_id("password").send_keys("secret_sauce")
        driver.find_element_by_css_selector("input[data-test='login-button']").click()
        assert driver.find_element_by_class_name("title").text == "PRODUCTS"
        driver.back()
        driver.forward()