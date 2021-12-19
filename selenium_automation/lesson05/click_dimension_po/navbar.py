import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Navbar():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get About Element in Navbar")
    def about(self):
        return self.driver.find_element(By.XPATH, "//a/span[text()='About']")

    @allure.step("Get Technology Section Element from About")
    def technology_section(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Our Technology']")

    @allure.step("Ignore popoup")
    def popup_ignore(self):
        return self.driver.find_element(By.XPATH, "//input[@type='button' and @value='OK']")

    @allure.step("Get Regional Button")
    def explore_regional(self):
        return self.driver.find_element(By.XPATH, "//a[@href='http://clickdimensions.com/partner-listing/']")
