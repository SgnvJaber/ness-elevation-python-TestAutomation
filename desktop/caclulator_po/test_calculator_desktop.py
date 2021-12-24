import allure
import pytest
from selenium import webdriver
from desktop.caclulator_po.calculator_page import Calculator_Page

class Test_Calculator_Desktop:

    def setup_class(cls):
        global driver
        desired_caps = {}
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        desired_caps["platformName"] = "Windows"
        desired_caps["deviceName"] = "WindowsPC"
        driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
        global calc
        calc = Calculator_Page(driver)
        driver.implicitly_wait(5)

    def teardown_method(cls):
        calc.action_clear_display()

    def teardown_class(cls):
        driver.quit()

    @allure.title("Verify The add operation")
    @allure.step("This test verify that the calculator add operation works as expected")
    def test__verify_add_operation(self):
        calc.action_operation("3", "+", "4")
        actual_result = float(3 + 4)
        calc_result = calc.action_get_operation_result()
        assert actual_result == calc_result

    @allure.title("Verify The add operation")
    @allure.step("This test verify that the calculator subtract operation works as expected")
    def test__verify_subtract_operation(self):
        calc.action_operation("3", "-", "4")
        actual_result = float(3 - 4)
        calc_result = calc.action_get_operation_result()
        assert actual_result == calc_result

    @allure.title("Verify The add operation")
    @allure.step("This test verify that the calculator divide operation works as expected")
    def test__verify_divide_operation(self):
        try:
            calc.action_operation("3", "/", "2")
            actual_result = float(3 / 2)
            calc_result = calc.action_get_operation_result()
            assert actual_result == calc_result
        except Exception as e:
            print("An Error Occurred...See details:", e)
            pytest.fail("Test Failed")

    @allure.title("Verify The add operation")
    @allure.step("This test verify that the calculator multiply operation works as expected")
    def test__verify_multiply_operation(self):
        calc.action_operation("3", "*", "5")
        actual_result = float(3 * 5)
        calc_result = calc.action_get_operation_result()
        assert actual_result == calc_result
