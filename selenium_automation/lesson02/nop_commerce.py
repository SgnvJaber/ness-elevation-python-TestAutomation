import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement

expected_total = 3
filter_by = "Price: Low to High"
expected_names = ["Nikon D5500 DSLR", "Leica T Mirrorless Digital Camera", "Apple iCam"]
expected_ratings = [0, 4, 5]

class Test_Nop_Commerce:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://demo.nopcommerce.com/")

    def teardown_class(cls):
        driver.quit()

    def test_verify_products_total(self):
        self.navigate_to_main_page()
        items = self.get_items()
        assert len(items) == expected_total

    def test_verify_products_names(self):
        self.navigate_to_main_page()
        names = self.get_items()
        self.assert_list(names, expected_names)

    def test_verify_products_rating(self):
        self.navigate_to_main_page()
        ratings = self.get_ratings()
        self.assert_list(ratings, expected_ratings)

    def navigate_to_main_page(self):
        driver.find_element(By.CSS_SELECTOR, "a[href='/electronics']").click()
        driver.set_page_load_timeout(10)
        driver.find_element(By.XPATH, "//div[@class='picture']/a[@href='/camera-photo']").click()
        my_filter = Select(driver.find_element(By.ID, "products-orderby"))
        my_filter.select_by_visible_text(filter_by)

    def get_items(self):
        items = driver.find_elements(By.XPATH, "//h2[@class='product-title']/a")
        values = []
        for item in items:
            values.append(item.text)
        return values

    def get_ratings(self):
        ratings = driver.find_elements(By.XPATH, "//div[@class='rating']/div")
        values = []
        for item in ratings:
            temp = item.get_attribute("style")
            # Removing the word 'width' and '%'
            temp = temp[7:len(temp) - 2]
            # 100%=5 stars,to get the number of stars,will be dividing the percentage by 20
            values.append(int(int(temp) / 20))
        print(values)
        return values

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
