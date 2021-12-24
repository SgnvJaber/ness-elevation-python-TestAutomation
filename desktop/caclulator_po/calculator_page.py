import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Calculator_Page():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get Given Number Element")
    def get_number_element(self, number_str):
        xpath = "//*[@AutomationId='num" + number_str + "Button']"
        return self.driver.find_element(By.XPATH, xpath)

    @allure.step("Get Equal element")
    def get_equal_element(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='equalButton']")

    @allure.step("Get Clear element")
    def get_clear_element(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='clearButton']")

    @allure.step("Get Result element")
    def get_result_element(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='CalculatorResults']")

    @allure.step("get operation element")
    def get_operation_element(self, operation):
        xpath = "//*[@AutomationId='" + operation + "Button']"
        return self.driver.find_element(By.XPATH, xpath)

    @allure.step("Convert give Operator to Calculator text")
    def convert_operation_to_calculator(self, operation):
        op_calculator = "plus"
        if (operation == "-"):
            op_calculator = "minus"
        elif (operation == "/"):
            op_calculator = "divide"
        elif (operation == "*"):
            op_calculator = "multiply"
        return op_calculator

    @allure.step("Calculator Operation on a given input")
    def action_operation(self, first_input, operation, second_input):
        if (operation == "/" and second_input == "0"):
            print("Cannot divide number by zero!")
            return

        operator = self.convert_operation_to_calculator(operation)
        first_input_element = self.get_number_element(first_input)
        operator_elem = self.get_operation_element(operator)
        second_input_element = self.get_number_element(second_input)
        first_input_element.click()
        operator_elem.click()
        second_input_element.click()
        self.get_equal_element().click()

    @allure.step("Get Result")
    def action_get_operation_result(self):
        result_text = self.get_result_element().text.split("Display is ")[1]
        return float(result_text)

    @allure.step("Clear Result")
    def action_clear_display(self):
        return self.get_clear_element().click()
