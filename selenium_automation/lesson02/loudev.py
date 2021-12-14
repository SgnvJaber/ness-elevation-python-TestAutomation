from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium_automation.lesson02.support import Support


class Test_Loudev:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("http://loudev.com")

    def teardown_class(cls):
        driver.quit()

    def test_01(self):
        support = Support()
        support.verify_elements(driver)
