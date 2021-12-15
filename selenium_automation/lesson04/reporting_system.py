
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

expected_welcome_text = "Welcome to your store!"


class Test_Reporting_System:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://admin-demo.nopcommerce.com")

    def teardown_class(cls):
        driver.quit()

    def attach_file(self, name):
        image = "./screen-shots/" + name + ".png"  # need to create folder: screen-shots first
        driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

    @allure.title("Verify Login")
    @allure.description("This test Verify Login Successfully")
    def test_verify_login(self):
        try:
            self.login()
            assert self.get_welcome_text() == expected_welcome_text
        except AssertionError as e:
            self.attach_file("test_verify_login")
            pytest.fail("Test Failed...see details:", e)

    @allure.step("Login Flow")
    def login(self):
        credentials = self.get_credentials()
        email_field = driver.find_element(By.XPATH, "//input[@type='email']")
        password_field = driver.find_element(By.XPATH, "//input[@type='password']")
        email_field.clear()
        password_field.clear()
        email_field.send_keys(credentials[0])
        password_field.send_keys(credentials[1])
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

    @allure.step("get credentials")
    def get_credentials(self):
        box = driver.find_element(By.XPATH, "//div[@class='topic-block-body']/p").text
        email = box.split("Admin email: ")[1].split("\n")[0]
        password = box.split("Admin password: ")[1]
        credentials = [email, password]
        return credentials

    @allure.step("get welcome to text ")
    def get_welcome_text(self):
        return driver.find_element(By.XPATH, "//div[@class='col-12']/h4").text
