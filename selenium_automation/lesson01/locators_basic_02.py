from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test_Locators_Basic_02:
    def setup_class(cls):
        global driver
        # Open Browser in english
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        driver.maximize_window()
        driver.get("https://www.wikipedia.org/")

    def teardown_class(cls):
        driver.quit()

    def test_verify_elements(self):
        list = []
        list.append(driver.find_element(By.CLASS_NAME, "central-featured-logo"))
        list.append(driver.find_element(By.ID, "searchInput"))
        list.append(driver.find_element(By.ID, "searchLanguage"))
        list.append(driver.find_element(By.CLASS_NAME, "footer-sidebar-content"))
        for item in list:
            print(item)
