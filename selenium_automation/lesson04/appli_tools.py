# NOTE RUN Using Selenium:3.141.0
import allure
from applitools.selenium import Eyes
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

eyes = Eyes()


class Test_Applitools:

    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://applitools.com/helloworld/")
        driver.implicitly_wait(5)
        eyes.api_key = 'mDtTzsEidmBygiKlFlF8pUkguoUSbj1zfk2QYVJlnVI110'

    @allure.title("Verify Applitools FLOW")
    @allure.description("This test verify Todo Operations:Create,Rename,Delete,Mark,Filter,And Remove All")
    def test_hello_world_logo(self):
        eyes.open(driver, "Test_Applitools", "Hello World")
        eyes.check_window('Initial Screen Shot')
        self.generate_random()
        self.change_logos_color()
        self.btn_click()

    @allure.step("Generate Number Number ")
    def generate_random(self):
        driver.find_element_by_link_text("?diff1").click()
        eyes.check_window('After Clicking ?diff1 Button')

    @allure.step("Generate Logo's Color")
    def change_logos_color(self):
        driver.find_element_by_link_text("?diff2").click()
        eyes.check_window('After Clicking ?diff2 Button')

    @allure.step("Click Button For Extra image Generation")
    def btn_click(self):
        driver.find_element_by_xpath("//div[@class='section button-section']/button").click()
        eyes.check_window('After Clicking Click me! Button')

    def teardown_class(self):
        eyes.close()
        driver.quit()
        eyes.abort()
