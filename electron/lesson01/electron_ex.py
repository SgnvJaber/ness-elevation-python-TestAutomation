import time

from selenium import webdriver
from selenium.webdriver.common.by import By

electron_app = 'C:\\Automation\\ElectronApiDemos\\ElectronApiDemos.exe'
edriver = 'C:\\Automation\\ElectronDriver\\electrondriver.exe'
expected_menu_size = 6


class Test_Ex:

    def setup_class(self):
        options = webdriver.ChromeOptions()
        options.binary_location = electron_app
        global driver
        driver = webdriver.Chrome(chrome_options=options, executable_path=edriver)
        driver.implicitly_wait(5)

    def test_01_electron(self):
        menu = driver.find_elements(By.XPATH, "//nav/div/h5")
        assert len(menu) == expected_menu_size

    def teardown_class(self):
        driver.quit()
