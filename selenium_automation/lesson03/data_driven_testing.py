import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

key_value = "input,expected"
my_list = [("Isreal", "Israel"), ("Automation", "Automation"), ("BlahBlah", "Search results")]


class Test_Actions_Ex:
    def setup_class(cls):
        global driver
        # Open Browser in english
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        driver.maximize_window()
        driver.get("https://www.wikipedia.org/")
        driver.implicitly_wait(10)

    def teardown_class(cls):
        driver.quit()

    def attach_file(self, name):
        image = "./screen-shots/" + name + ".png"  # need to create folder: screen-shots first
        driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

    @allure.title("Verify Search Result Using DDT")
    @allure.description("This test Verify the Wiki search bar")
    @pytest.mark.parametrize(key_value, my_list)
    def test_verify_search_bar(self, input, expected):
        driver.find_element(By.ID, "searchInput").send_keys(input)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        text = driver.find_element(By.ID, "firstHeading").text
        driver.get("https://www.wikipedia.org/")
        assert text == expected
