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

    @allure.step("Get the navbar list of elements")
    def navbar_list(self):
        return self.driver.find_elements(By.XPATH, "//ul[@id='mainMenuFirstLevelUnorderedList']/li")

    @allure.step("Get Current Menu Element")
    def current_menu(self):
        return self.driver.find_element(By.XPATH, "//li[@class='current main-menu-first-level-list-item']")

    @allure.step("Get Recruitment_tab")
    def recruitment_menu(self):
        return self.driver.find_element(By.ID, "menu_recruitment_viewRecruitmentModule")

    @allure.step("Get Admin tab")
    def admin_menu(self):
        return self.driver.find_element(By.ID, "menu_admin_viewAdminModule")

    @allure.step("Get Job tab")
    def job_menu(self):
        return self.driver.find_element(By.ID, "menu_admin_Job")

    @allure.step("Get Job tab")
    def work_shifts_menu(self):
        return self.driver.find_element(By.ID, "menu_admin_workShift")

    @allure.step("Return the number of tabs")
    def action_get_tabs_size(self):
        return len(self.navbar_list())

    @allure.step("Return the number of tabs")
    def action_get_default_tab(self):
        return self.current_menu().text

    @allure.step("Navigate To Recruitment")
    def action_navigate_to_recruitment(self):
        self.recruitment_menu().click()

    @allure.step("Navigate To Work Shift")
    def action_navigate_to_work_shift(self):
        self.admin_menu().click()
        self.job_menu().click()
        self.work_shifts_menu().click()

