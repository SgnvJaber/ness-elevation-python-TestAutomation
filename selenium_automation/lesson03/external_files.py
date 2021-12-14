import time
import xml.etree.ElementTree as ET

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_data(node_name):
    root = ET.parse("C:/Automation/Python/test_automation/selenium_automation/lesson03/configuration.xml").getroot()
    return root.find(".//" + node_name).text


class Test_External_Files:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(get_data("Url"))

    def teardown_class(cls):
        driver.quit()

    def test_verify_result(self):
        self.fill_details(get_data("Weight"), get_data("Height"))
        self.calculate()
        result = driver.find_element(By.XPATH, "//input[@id='bmi_result']").get_attribute("value")
        assert result == get_data("ExpectedResultBMI")

    def test_verify_means(self):
        means = driver.find_element(By.XPATH, "//input[@id='bmi_means']").get_attribute("value")
        assert means == get_data("ExpectedMeans")

    def fill_details(self, weight, height):
        driver.find_element(By.XPATH, "//input[@name='weight']").send_keys(weight)
        driver.find_element(By.XPATH, "//input[@name='height']").send_keys(height)

    def calculate(self):
        driver.find_element(By.XPATH, "//input[@id='calculate_data']").click()
