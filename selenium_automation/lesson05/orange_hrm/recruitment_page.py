import allure
from selenium.webdriver.common.by import By


class Recruitment_Page():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get Date From field Element")
    def get_from_field(self):
        return self.driver.find_element(By.ID, "candidateSearch_fromDate")

    @allure.step("Get Date To field Element")
    def get_to_field(self):
        return self.driver.find_element(By.ID, "candidateSearch_toDate")

    @allure.step("Get Search button")
    def get_search_button(self):
        return self.driver.find_element(By.ID, "btnSrch")

    @allure.step("Get Date Search Result")
    def get_result(self):
        return self.driver.find_element(By.XPATH, "//tr/td")

    @allure.step("Get Date Flow:")
    def action_get_date(self, date_start, date_end):
        self.get_from_field().send_keys(date_start)
        self.get_to_field().send_keys(date_end)
        self.get_search_button().click()
        return self.get_result().text



