import allure
from selenium.webdriver.common.by import By


class Login_Page():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get Username field Element")
    def get_username_field(self):
        return self.driver.find_element(By.NAME, "username2")

    @allure.step("Get Password field Element")
    def get_password_field(self):
        return self.driver.find_element(By.NAME, "password2")

    @allure.step("Get submit Button")
    def submit(self):
        return self.driver.find_element(By.ID, "submit")

    @allure.step("Sign in Flow:")
    def action_sign_in(self, username, password):
        self.get_username_field().send_keys(username)
        self.get_password_field().send_keys(password)
        self.submit().click()
