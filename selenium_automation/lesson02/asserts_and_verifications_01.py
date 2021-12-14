from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement

expected_result = "34"
expected_means = "That you have overweight."


class Test_Asserts_And_Verifications_01:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/bmi/")

    def teardown_class(cls):
        driver.quit()

    def test_verify_result(self):
        self.fill_details("90", "163")
        self.calculate()
        result = driver.find_element(By.XPATH, "//input[@id='bmi_result']").get_attribute("value")
        assert result == expected_result


    def test_verify_means(self):
        means = driver.find_element(By.XPATH, "//input[@id='bmi_means']").get_attribute("value")
        assert means == expected_means


    def fill_details(self, weight, height):
        driver.find_element(By.XPATH, "//input[@name='weight']").send_keys(weight)
        driver.find_element(By.XPATH, "//input[@name='height']").send_keys(height)


    def calculate(self):
        driver.find_element(By.XPATH, "//input[@id='calculate_data']").click()

