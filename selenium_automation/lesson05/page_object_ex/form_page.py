import allure
from selenium.webdriver.common.by import By


class Form_Page():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get Occupation field Element")
    def get_occupation(self):
        return self.driver.find_element(By.ID, "occupation")

    @allure.step("Get Age field Element")
    def get_age(self):
        return self.driver.find_element(By.ID, "age")

    @allure.step("Get Location field Element")
    def get_location(self):
        return self.driver.find_element(By.ID, "location")

    @allure.step("Get submit Button")
    def submit(self):
        return self.driver.find_element(By.XPATH, "//input[@type='button']")

    @allure.step("Fill Form Flow:")
    def action_fill_form(self, occupation, age, location):
        self.get_occupation().send_keys(occupation)
        self.get_age().send_keys(age)
        self.get_location().send_keys(location)
        self.submit().click()
