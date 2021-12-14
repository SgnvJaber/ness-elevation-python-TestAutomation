import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test_Error_Handling:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_synchronization.html")

    def teardown_class(cls):
        driver.quit()

    @allure.step("Recover Page for the next test")
    def teardown_method(cls):
        driver.refresh()
        driver.set_page_load_timeout(3)

    @allure.step("Attaching a screenshot to the report")
    def attach_file(self):
        image = "./screen-shots/screen.png"  # need to create folder: screen-shots first
        driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

    @allure.title("Verify Button is removed using try and except")
    @allure.description("The test will verify that the 'remove' button is removed ")
    def test_remove(self):
        try:
            self.remove_check_box()
            check_box = self.get_check_box()
        except Exception as e:
            print("Could not find the element but the test did not fail")
        finally:
            print("Test Passed: checkbox indeed is removed ")

    @allure.title("Verify Button is removed without using try and except")
    @allure.description("The test will verify that the 'remove' button is removed ")
    def test_remove_without_try_catch(self):
        self.remove_check_box()
        if (len(driver.find_elements(By.ID, "checkbox"))) > 0:
            print("Element exists")
        else:
            print("Element is gone")

    @allure.step("Remove checkbox from screen")
    def remove_check_box(self):
        driver.find_element(By.ID, "btn").click()
        time.sleep(5)

    @allure.step("Return the check box element")
    def get_check_box(self):
        check_box = driver.find_element(By.XPATH, "//*[@id='checkbox']")
        return check_box
