from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test_Locators_Advanced:
    def setup_class(cls):
        global driver
        # Open Browser in english
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_locators.html")

    def teardown_class(cls):
        driver.quit()

    def test_verify_find_locators(self):
        elements = []
        elements.append(driver.find_element(By.ID, "locator_id"))
        elements.append(driver.find_element(By.NAME, "locator_name"))
        elements.append(driver.find_element(By.TAG_NAME, "p"))
        elements.append(driver.find_element(By.CLASS_NAME, "locator_class"))
        elements.append(driver.find_element(By.LINK_TEXT, "myLocator(5)"))
        elements.append(driver.find_element(By.PARTIAL_LINK_TEXT, "locator (6)"))
        elements.append(driver.find_element(By.XPATH, "//input[@myname='selenium']"))
        elements.append(driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-2']"))
        for element in elements:
            if (element.tag_name != "input"):
                print(element.text)
            else:
                print(element.get_attribute("value"))
