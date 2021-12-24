import time
import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from smart_assertions import soft_assert, verify_expectations

from selenium_automation.lesson05.orange_hrm.login_page import Login_Page
from selenium_automation.lesson05.orange_hrm.navbar import Navbar
from selenium_automation.lesson05.orange_hrm.recruitment_page import Recruitment_Page
from selenium_automation.lesson05.orange_hrm.work_shifts import Work_Shifts

expected_tabs_size = 11
expected_message = "No Records Found"


class Test_Orange_HRM:
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    loginp = Login_Page(driver)
    navb = Navbar(driver)
    recruit = Recruitment_Page(driver)
    shifts = Work_Shifts(driver)

    def setup_class(cls):
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com")
        driver.implicitly_wait(10)
        cls.loginp.action_sign_in("Admin", "admin123")

    def teardown_class(cls):
        driver.quit()

    def attach_file(self, name):
        image = "./screen-shots/" + name + ".png"  # need to create folder: screen-shots first
        driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

    @allure.title("Verify Navbar Default tab and size are as expected")
    @allure.step("This test verify the size of the navbar and its default tab")
    def test_verify_tabs_size_and_default(self):
        soft_assert(self.navb.action_get_tabs_size(), 11)
        soft_assert(self.navb.action_get_default_tab, "Dashboard")
        verify_expectations()

    @allure.title("Verify Invalid Date Message")
    @allure.step("This test verify that the Date Picker sends warning on inserting invalid date")
    def test_verify_invalid_date(self):
        self.navb.action_navigate_to_recruitment()
        response = self.recruit.action_get_date("25,10,2015", "1/1/1970")
        assert (response == expected_message)

    @allure.title("Export CSV")
    @allure.step("This test create CSV File from table")
    def test_verify_csv_export(self):
        self.navb.action_navigate_to_work_shift()
        self.shifts.action_export_table_to_CSV()
