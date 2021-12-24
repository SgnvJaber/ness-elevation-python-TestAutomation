import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

from selenium_automation.lesson05.page_object_ex.click_page import Click_Page
from selenium_automation.lesson05.page_object_ex.form_page import Form_Page
from selenium_automation.lesson05.page_object_ex.login_page import Login_Page

username = "selenium"
password = "webdriver"
occupation = "QA"
age = "25"
location = "Abu Ghosh"


class Test_Actions_Ex:
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    cp = Click_Page(driver)
    fp = Form_Page(driver)
    lp = Login_Page(driver)

    action = ActionChains(driver)

    def setup_class(cls):
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/webdriveradvance.html")
        driver.implicitly_wait(10)

    def teardown_class(cls):
        driver.quit()

    def attach_file(self, name):
        image = "./screen-shots/" + name + ".png"  # need to create folder: screen-shots first
        driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

    @allure.title("Verify Login")
    @allure.description("This test verify that login is valid")
    def test_verify_login(self):
        self.lp.action_sign_in(username, password)
        self.fp.action_fill_form(occupation, age, location)
        assert self.cp.action_is_displayed()
