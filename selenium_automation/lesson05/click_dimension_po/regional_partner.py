import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Regional_Partner():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Search for a given Partner in Central America")
    def get_partner_if_exist_in_central(self, partner):
        xPath = "//div[contains(@class,'central-america-caribbean')]//p[text()='" + partner + "']"
        return self.driver.find_elements(By.XPATH,xPath)
