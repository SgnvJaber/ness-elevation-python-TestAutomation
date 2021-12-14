import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
alert_text = "Alert is gone."
prompt = "Saed Jaber"
expected_frame_text = "This is an IFrame !"
expected_tab_text = "This is a new tab"


class Test_Switch_And_Navigation:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_switch_navigation.html")

    def teardown_class(cls):
        driver.quit()

    def test_verify_show_alert(self):
        driver.find_element(By.XPATH, "//input[@id='btnAlert']").click()
        popup = driver.switch_to.alert
        print(popup.text)
        popup.accept()
        output = self.get_output()
        assert output == alert_text

    def test_verify_show_prompt(self):
        driver.find_element(By.XPATH, "//input[@id='btnPrompt']").click()
        popup = driver.switch_to.alert
        print(popup.text)
        popup.send_keys(prompt)
        popup.accept()
        output = self.get_output()
        assert output == prompt


    def test_verify_open_tap_button(self):
        parent_handle = driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH, "//input[@id='btnNewTab']").click()
        win_handles = driver.window_handles
        driver.switch_to.window(win_handles[1])
        actual_text = driver.find_element(By.XPATH, "//div[@id='new_tab_container']").text
        driver.switch_to.window(win_handles[0])
        assert actual_text == expected_tab_text






    def test_verify_show_IFrame(self):
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)
        iframe_div = driver.find_element(By.XPATH, ("//div[@id='iframe_container']"))
        actual_text = iframe_div.text
        driver.switch_to.parent_frame()
        assert actual_text == expected_frame_text




    def get_output(self):
        result = driver.find_element(By.XPATH, "//span[@id='output']").text
        return result
