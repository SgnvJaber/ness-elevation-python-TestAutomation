import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

expected_title = "IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows"
expected_url = "https://www.imdb.com/"

@pytest.mark.usefixtures("init_driver")
class Test_IMDB:
    def test_verify_imdb(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.imdb.com/")
        driver.refresh()
        title = driver.title
        print(title)
        assert title == expected_title
        url = driver.current_url
        print(url)
        assert url == expected_url