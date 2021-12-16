import time
import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from smart_assertions import soft_assert, verify_expectations

my_max = 150


class Test_Actions_Ex:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.wooloverslondon.com")
        driver.implicitly_wait(10)
        global action
        action = ActionChains(driver)

    def teardown_class(cls):
        driver.quit()

    def attach_file(self, name):
        image = "./screen-shots/" + name + ".png"  # need to create folder: screen-shots first
        driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

    @allure.title("Verify Prices FLOW")
    @allure.description(
        "This test showcase the flow to obtain the prices and verify that they don't exceed a given max")
    def test_verify_prices(self):
        self.close_popup()
        self.navbar_new_in_click()
        self.change_currency("US Dollar")
        self.filter_by_men()
        self.sort_low_to_high()
        prices = self.get_prices()
        self.soft_assert_prices(prices, my_max)

    @allure.step("Change currency")
    def change_currency(self, currency):
        driver.find_element(By.XPATH, "//span/img").click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//select[@id='gle_selectedCountry']")))
        currencies = driver.find_element(By.XPATH, "//select[@id='gle_selectedCurrency']")
        select_field = Select(currencies)
        select_field.select_by_visible_text(currency)
        driver.find_element(By.XPATH, "//input[@data-key='SavenClose']").click()
        time.sleep(0.5)

    @allure.step("Click on Step in in the navbar")
    def navbar_new_in_click(self):
        driver.find_element(By.XPATH, "//li[@class='dropdown hasSubmenu New Arrivals']/a").click()

    @allure.step("Close the popup")
    def close_popup(self):
        driver.find_element(By.XPATH, "//span[@class='glClose']").click()

    @allure.step("Filter By men")
    def filter_by_men(self):
        driver.find_element(By.XPATH, "//button[@id='dd-Gender']").click()
        driver.find_element(By.XPATH, "//span[text()='Men']").click()
        driver.find_element(By.XPATH, "//span[text()='Women']").click()
        driver.find_element(By.CLASS_NAME, "js-toggle-close-all").click()

    @allure.step("Sort Prices from low to high")
    def sort_low_to_high(self):
        driver.find_element(By.XPATH, "//button[@id='dd-Sort By']").click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Price Low to High']")))
        driver.find_element(By.XPATH, "//span[text()='Price Low to High']").click()
        driver.refresh()

    @allure.step("Get Product Prices:")
    def get_prices(self):
        prices_elements = driver.find_elements(By.XPATH, "//span[@class='pricing__price pricing__price--new']")
        prices = []
        for elem in prices_elements:
            if not elem.text == "":
                prices.append(float(elem.text[2:]))
        return prices

    def soft_assert_prices(self, prices, max):
        for price in prices:
            soft_assert(price < max)
        verify_expectations()
