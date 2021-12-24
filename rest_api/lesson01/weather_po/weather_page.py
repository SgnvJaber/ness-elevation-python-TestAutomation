import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Weather_Page():

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get search field Element")
    def get_search_field(self):
        return self.driver.find_element(By.XPATH, "//input[@name='q']")

    @allure.step("Get search results Elements")
    def get_search_results(self):
        return self.driver.find_elements(By.XPATH, "//tbody/tr/td/b/a")

    @allure.step("Get Humidity element")
    def get_humidity_element(self):
        return self.driver.find_element(By.XPATH, "//*[@id='weather-widget']/div[2]/div[1]/div[1]/div[2]/ul/li[3]")

    @allure.step("Sign in Flow:")
    def action_get_humidity(self, city):
        time.sleep(5)
        self.get_search_field().send_keys(city)
        self.get_search_field().send_keys(Keys.ENTER)
        list = self.get_search_results()
        list[0].click()
        time.sleep(5)
        # Cutting "Humidity\n" and the "%" from the output
        output = self.get_humidity_element().text.split("\n")[1]
        output = output[:len(output) - 1]
        return output
