from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test_Locators_Basic_01:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.selenium.dev/")

    def teardown_class(cls):
        driver.quit()


    def test_verify_logo(self):
        print(driver.find_element(By.ID, "selenium_logo"))
        print(driver.find_element(By.CLASS_NAME, "navbar-brand"))
        print(driver.find_element(By.CLASS_NAME, "navbar-logo"))
        print(driver.find_element(By.TAG_NAME, "svg"))
        print(driver.find_elements(By.TAG_NAME, "svg")[0])

    def test_verify_number_of_links(self):
        links = driver.find_elements(By.TAG_NAME, "a")
        print("links number:" + str(len(links)))

    def test_verify_number_of_links_with_selenium_upper(self):
        links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Selenium")
        print("links number:" + str(len(links)))

    def test_verify_number_of_links_with_selenium_lower(self):
        links = driver.find_elements(By.PARTIAL_LINK_TEXT, "selenium")
        print("links number:" + str(len(links)))
