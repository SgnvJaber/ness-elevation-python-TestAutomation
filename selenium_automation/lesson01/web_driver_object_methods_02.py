from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Test_Web_Driver_Object_Methods_02:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.google.com/")

    def teardown_class(cls):
        driver.quit()

    def test_verify_navigation(self):
        driver.get("https://www.bing.com/")
        driver.back()
        print("Title is:"+driver.title)

    def test_verify_bubbles(self):
        driver.get("https://www.google.com/")
        word="bubble"
        if(word in driver.page_source):
            print("Exist")
        else:
            print("Not Exist")

