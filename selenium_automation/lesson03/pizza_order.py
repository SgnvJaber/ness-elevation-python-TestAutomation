import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


#Data to provide for the system
alert_text = "Alert is gone."
prompt = "Saed Jaber"
expected_frame_text = "This is an IFrame !"
expected_tab_text = "This is a new tab"

first_name = "Saed"
last_name = "Jaber"
my_choice = "Delivery|3"
expected_initial_price = "$7.50"
expected_updated_price = "$10.50"


class Test_Pizza_Order:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/pizza/")

    def teardown_class(cls):
        driver.quit()

    def teardown_method(self, cls):
        self.clear_details()

    @allure.title("Verify initial Price")
    @allure.description("This test verify the initial price is as expected before adding any items")
    def test_verify_initial_price(self):
        try:
            initial_price = self.get_price()
            assert initial_price == expected_initial_price
        except AssertionError as e:
            self.attach_file()
            pytest.fail("Test Failed...see details:", e)

    @allure.title("Verify Price Update")
    @allure.description("This test verify the  price changed after adding delivery")
    def test_verify_updated_price(self):
        try:
            self.select_delivery(my_choice)
            updated_price = self.get_price()
            assert updated_price == expected_updated_price
        except AssertionError as e:
            self.attach_file()
            pytest.fail("Test Failed...see details:", e)

    @allure.title("Verify Coupon applied")
    @allure.description("This test verify that coupon is applied to the price")
    def test_verify_coupon(self):
        try:
            self.fill_details(first_name, last_name)
            my_coupon = self.get_coupon()
            text = self.get_alert_text()
            assert text == first_name + " " + last_name + " " + my_coupon
        except AssertionError as e:
            self.attach_file()
            pytest.fail("Test Failed...see details:", e)

    @allure.step("Getting the price output")
    def get_price(self):
        return driver.find_element(By.CSS_SELECTOR, "span[class='ginput_total ginput_total_5']").text

    @allure.step("Getting the text inside the pop up alert")
    def get_alert_text(self):
        driver.find_element(By.CSS_SELECTOR, "input[id='gform_submit_button_5']").click()
        popup = driver.switch_to.alert
        text = popup.text
        popup.accept()
        return text

    @allure.step("Getting the coupon from the iframe")
    def get_coupon(self):
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)
        coupon = driver.find_element(By.CSS_SELECTOR, "div[id='coupon_Number']").text
        driver.switch_to.parent_frame()
        driver.find_element(By.CSS_SELECTOR, "textarea[id='input_5_20']").send_keys(coupon)
        return coupon

    @allure.step("Filling first name and last name inside their corresponding fields")
    def fill_details(self, fname, lname):
        fname_field = driver.find_element(By.CSS_SELECTOR, "input[name='input_22.3']")
        lname_field = driver.find_element(By.CSS_SELECTOR, "input[name='input_22.6']")
        fname_field.send_keys(fname)
        lname_field.send_keys(lname)

    @allure.step("Clearing details for next test")
    def clear_details(self):
        driver.find_element(By.CSS_SELECTOR, "input[name='input_22.3']").clear()
        driver.find_element(By.CSS_SELECTOR, "input[name='input_22.6']").clear()

    @allure.step("Selecting delivery by choice")
    def select_delivery(self, choice):
        selection = Select(driver.find_element(By.ID, "input_5_21"))
        selection.select_by_value(choice)

    @allure.step("Getting the price output")
    def get_output(self):
        result = driver.find_element(By.XPATH, "//span[@id='output']").text
        return result

    @allure.step("Attaching a screenshot to the report")
    def attach_file(self):
        image = "./screen-shots/screen.png"  # need to create folder: screen-shots first
        driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
