import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

expected_output = "My Rendered Element After Fact!"


class Test_Synchronization:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_synchronization.html")

    def teardown_class(cls):
        driver.quit()

    def test_01_explicitly_wait(self):
        driver.find_element(By.ID, "rendered").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "finish2")))
        output = driver.find_element(By.ID, "finish2").text
        assert output == expected_output

    def test_02_sleep(self):
        driver.find_element(By.ID, "hidden").click()
        time.sleep(1)
        assert driver.find_element(By.ID, "loading1").is_displayed()

    def test_03_implicitly_wait(self):
        driver.find_element(By.XPATH, "//button[text()='Remove']").click()
        driver.implicitly_wait(10)
        text = driver.find_element(By.XPATH, "//p[@id='message']")
        assert text.is_displayed()
