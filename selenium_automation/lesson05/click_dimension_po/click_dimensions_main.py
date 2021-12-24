import time
import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from smart_assertions import soft_assert, verify_expectations

from selenium_automation.lesson05.click_dimension_po.navbar import Navbar
from selenium_automation.lesson05.click_dimension_po.regional_partner import Regional_Partner

partner_search = "C-ven Technologies"


class Test_Click_Dimension:
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    nav = Navbar(driver)
    rp = Regional_Partner(driver)
    action = ActionChains(driver)

    def setup_class(cls):
        driver.maximize_window()
        driver.get("https://clickdimensions.com")
        driver.implicitly_wait(10)

    def teardown_class(cls):
        driver.quit()

    def attach_file(self, name):
        image = "./screen-shots/" + name + ".png"  # need to create folder: screen-shots first
        driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

    @allure.title("Verify Partner exist in Central America")
    @allure.description("This test verify a given Partner is inside Centeral America")
    def test_if_partner_exist_in_central(self):
        list = self.get_partner_in_central_america(partner_search)
        assert len(list) > 0

    @allure.step("Navigate To Regional Section:")
    def get_partner_in_central_america(self, partner):
        self.action.move_to_element(self.nav.about()).perform()
        self.nav.technology_section().click()
        self.nav.popup_ignore().click()
        self.nav.explore_regional().click()
        driver.set_page_load_timeout(5)
        list = self.rp.get_partner_if_exist_in_central(partner)
        return list
