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
min = "2"
max = "6"


class Test_Super_Calculator_V2:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.random.org/")

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
            random = self.get_random_number()
            self.calculate(random)
            self.print_result(random)
        except Exception as e:
            self.attach_file()
            pytest.fail("An error has occurred...see details:", e)

    @allure.step("Calculate until provided number")
    def calculate(self, random):
        self.navigate_to_calculator()
        temp = random - 1
        while (temp >= 0):
            self.fill_input(random, my_operator, int(temp))
            time.sleep(wait_time)
            temp -= 1

    @allure.step("Generate Random Number")
    def generate_random_number(self, min_number, max_number):

        if (min_number > max_number):
            mini = max_number
            max_number = min_number
            min_number = mini

        first_input = driver.find_element(By.CSS_SELECTOR, "input[id$='min']")
        first_input.clear()
        first_input.send_keys(min_number)
        second_input = driver.find_element(By.CSS_SELECTOR, "input[id$='max']")
        second_input.clear()
        second_input.send_keys(max_number)
        driver.find_element(By.XPATH, "//input[@value='Generate']").click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//center/span[1]")))

    @allure.step("Store the Random Number")
    def get_random_number(self):
        self.navigate_to_iframe()
        self.generate_random_number(min, max)
        rand = driver.find_element(By.XPATH, "//center/span[1]").text
        return int(rand)

    @allure.step("Navigate to Calculator")
    def navigate_to_calculator(self):
        driver.get("https://juliemr.github.io/protractor-demo/")

    @allure.step("Navigate inside the iframe")
    def navigate_to_iframe(self):
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)

    @allure.step("Filling inputs")
    def fill_input(self, first_value, operator, second_value):
        operation = Select(driver.find_element(By.XPATH, "//select[@ng-model='operator']"))
        operation.select_by_visible_text(operator)
        driver.find_element(By.XPATH, "//input[@ng-model='first']").send_keys(first_value)
        driver.find_element(By.XPATH, "//input[@ng-model='second']").send_keys(second_value)
        driver.find_element(By.XPATH, "//button[@id='gobutton']").click()

    @allure.step("Print Result of calculation")
    def print_result(self, random):
        td = driver.find_elements(By.XPATH, "//td[@class='ng-binding']")
        sum = 0
        for i in range(1, len(td), 2):
            sum += int(td[i].text)
        print("The Random Number is: " + str(random))
        print("The result for Number: " + str(random) + " is: " + str(sum))
