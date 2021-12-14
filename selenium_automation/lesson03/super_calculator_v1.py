import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

my_operator = "*"
wait_time = 2
max = 3


class Test_Super_Calculator_V1:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://juliemr.github.io/protractor-demo/")

    def teardown_class(cls):
        driver.quit()

    @allure.step("Attaching a screenshot to the report")
    def attach_file(self):
        image = "./screen-shots/screen.png"  # need to create folder: screen-shots first
        driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

    @allure.title("Verify Calculation")
    @allure.description("The function will keep calculating until provided number")
    def test_calculate(self):
        try:
            self.calculate(max)
            self.print_input()
        except Exception as e:
            self.attach_file()
            pytest.fail("An error has occurred...see details:", e)

    @allure.step("Filling inputs")
    def fill_input(self, first_value, operator, second_value):
        operation = Select(driver.find_element(By.XPATH, "//select[@ng-model='operator']"))
        operation.select_by_visible_text(operator)
        driver.find_element(By.XPATH, "//input[@ng-model='first']").send_keys(first_value)
        driver.find_element(By.XPATH, "//input[@ng-model='second']").send_keys(second_value)
        driver.find_element(By.XPATH, "//button[@id='gobutton']").click()

    @allure.step("Calculate until provided number")
    def calculate(self, max_number):
        for i in range(1, max_number + 1):
            for j in range(1, max_number + 1):
                self.fill_input(str(i), my_operator, str(j))
                time.sleep(wait_time)

    @allure.step("Print Results of calculation")
    def print_input(self):
        td = driver.find_elements(By.XPATH, "//td[@class='ng-binding']")
        for i in range(1, len(td), 2):
            print(td[i].text)

