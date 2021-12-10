from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

expected_title = "IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows"
expected_url = "https://www.imdb.com/"


class Test_Web_Driver_Object_Methods_01:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.imdb.com/")

    def teardown_class(cls):
        driver.quit()

    def test_verify_imdb(self):
        driver.refresh()
        title = driver.title
        print(title)
        if (title == expected_title):
            print("Test Passed")
        else:
            print("Test Failed")
        url = driver.current_url
        print(url)
        if (url == expected_url):
            print("Url Passed")
        else:
            print("URL Failed")
