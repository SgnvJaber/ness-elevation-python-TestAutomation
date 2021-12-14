import allure
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

expected_size = 9
expected_min_price = 10
expected_quantity = 1
products = "Hoodie"
item_to_click = "Invertocat Hoodie"


class Test_GitHub_Shop:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://thegithubshop.com/")

    @allure.step("Clear input for next test")
    def teardown_method(self, cls):
        self.search_clear()

    def teardown_class(cls):
        driver.quit()

    @allure.step("Attaching a screenshot to the report")
    def attach_file(self):
        image = "./screen-shots/screen.png"  # need to create folder: screen-shots first
        driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

    @allure.title("Verify The number of results")
    @allure.description("This test verifies that the number of results is as expected")
    def test_verify_results_(self):
        self.search(products)
        items = self.get_items()
        assert len(items) == expected_size

    @allure.title("Verify Price are above the minimum expected price")
    @allure.description("This test verifies that the all products prices are large than the minimum")
    def test_verify_prices(self):
        self.search(products)
        prices = self.get_prices()
        prices.sort()
        actual_min = float(prices[0].replace("$", ""))
        assert actual_min > expected_min_price

    @allure.title("Verify The initial Quantity is as expected")
    @allure.description("This test verifies that the the initial quantity of a given product is as expected")
    def test_verify_quantity(self):
        self.search(products)
        items = self.get_items()
        self.click_on_item_if_exist(items, item_to_click)
        actual_quantity = int(self.get_current_quantity())
        assert actual_quantity == expected_quantity

    @allure.step("Search for an item provided by keyword")
    def search(self, keyword):
        elem = driver.find_elements(By.XPATH, "//input[@type='search']")[1]
        elem.send_keys(keyword)
        elem.send_keys(Keys.ENTER)

    @allure.step("Clear Search input")
    def search_clear(self):
        elem = driver.find_elements(By.XPATH, "//input[@type='search']")[1]
        elem.clear()

    @allure.step("Click on item page if it exists")
    def click_on_item_if_exist(self, items, item):
        if (item in items):
            items_elements = driver.find_elements(By.XPATH, "//div[@class='product-thumbnail easylockdown-item']/a/h3")
            for elem in items_elements:
                if (elem.text == item):
                    elem.click()
                    break

    @allure.step("Get the current quantity")
    def get_current_quantity(self):
        return driver.find_element(By.XPATH, "//input[@id='Quantity']").get_attribute("value")

    @allure.step("Return search result")
    def get_items(self):
        items = self.get_text_from_list("//div[@class='product-thumbnail easylockdown-item']/a/h3")
        return items

    @allure.step("Return all products prices")
    def get_prices(self):
        prices = self.get_text_from_list("//span[@class='product-thumbnail__price__cost']")
        return prices

    @allure.step("Calling a generic function that takes xpath as in input that returns a list")
    def get_text_from_list(self, xpath):
        elements = driver.find_elements(By.XPATH, xpath)
        list = []
        for elem in elements:
            list.append(elem.text)
        return list
