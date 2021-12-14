import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

expected_value = "Calculate BMI"
expected_tag = "input"
expected_size = [133, 35]
expected_coordinate = [396, 265]


class Test_Asserts_And_Verifications_02:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/bmi/")

    def teardown_class(cls):
        driver.quit()

    def test_verify_size(self):
        size = self.get_size()
        sizes = [size["width"], size["height"]]
        print(expected_size)
        print(sizes)
        self.assert_list(sizes, expected_size)

    def test_verify_coordinate(self):
        coordinate = self.get_location()
        print(coordinate)
        coordinates = [coordinate["x"], coordinate["y"]]
        self.assert_list(coordinates, expected_coordinate)

    def test_verify_enabled(self):
        assert driver.find_element(By.XPATH, "//input[@id='calculate_data']").is_enabled()

    def test_verify_displayed(self):
        assert driver.find_element(By.XPATH, "//input[@id='calculate_data']").is_displayed()

    def test_verify_selected(self):
        assert not driver.find_element(By.XPATH, "//input[@id='calculate_data']").is_selected()

    def test_verify_tag_value(self):
        assert driver.find_element(By.XPATH, "//input[@id='calculate_data']").get_attribute("value") == expected_value

    def test_verify_hidden_dive(self):
        assert not driver.find_element(By.XPATH, "//div[@id='new_input']").is_displayed()

    def get_size(self):
        return driver.find_element(By.XPATH, "//input[@id='calculate_data']").size

    def get_location(self):
        return driver.find_element(By.XPATH, "//input[@id='calculate_data']").location

    def assert_list(self, alist, blist):
        fail_test = False
        if len(alist) != len(blist):
            pytest.fail("list size don't match")
        for i in range(len(alist)):
            try:
                assert alist[i] == blist[i]
            except Exception as e:
                fail_test = True
                print("\nExpected:" + alist[i] + "\nActual:" + blist[i])

        if (fail_test):
            pytest.fail("Test Failed!!")
