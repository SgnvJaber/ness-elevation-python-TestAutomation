import allure
from selenium.webdriver.common.by import By


class Click_Page():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get Click Button Element")
    def get_click_button(self):
        return self.driver.find_element(By.XPATH, "//button[@type='button']")

    @allure.step("Click On Button")
    def click(self):
        return self.get_click_button.click()

    @allure.step("Check if Button is displayed")
    def action_is_displayed(self):
        return self.get_click_button().is_displayed()
