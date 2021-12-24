import os

import allure
from selenium import webdriver
from smart_assertions import soft_assert, verify_expectations
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from cl_automation.edge_fix import EdgeChromiumDriverManager

expected_title = "IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows"
expected_url = "https://www.imdb.com/"


class Test_Imdb:
    def setup_class(cls):
        global driver
        browser_type = os.getenv("BrowserType")
        browser_type = "edge"
        if (browser_type):
            if (browser_type.lower() == 'chrome'):
                driver = webdriver.Chrome(ChromeDriverManager().install())
            elif (browser_type.lower() == 'edge'):
                driver = webdriver.Edge(EdgeChromiumDriverManager().install())
            elif (browser_type.lower() == 'firefox'):
                driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            raise Exception("Wrong Browser Type!")

        driver.maximize_window()
        driver.get("https://www.imdb.com/")

    def teardown_class(cls):
        driver.quit()

    @allure.step("Verify IMDB Title and Url using Soft Assert")
    def test_verify_imdb(self):
        driver.refresh()
        title = driver.title
        url = driver.current_url
        print(title)
        print(url)
        soft_assert(title == expected_title)
        soft_assert(url == expected_url)
        verify_expectations()
