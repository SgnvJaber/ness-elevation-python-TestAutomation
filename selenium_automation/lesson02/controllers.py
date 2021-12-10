from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

first_name = "Saed"
last_name = "Jaber"
continent = "europe"
command = "Switch Commands"


class Test_Controllers:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_controllers.html")

    def teardown_class(cls):
        driver.quit()

    def test_verify_url_contain_name(self):
        self.fill_full_name()
        self.fill_drop_down()
        self.fill_automation_tool()
        self.fill_profession()
        self.fill_selenium_commands()
        self.fill_year_of_experience()
        self.file_upload()
        self.submit_button()
        url = driver.current_url
        if (first_name in url and last_name in url):
            print("Test Passed")
        else:
            print("Test Failed")

    def test_verify_url_contain_date(self):
        self.fill_date()
        self.submit_button()
        url = driver.current_url
        if ("19" in url):
            print("Test Passed")
            # Yoni's idea
            line = url.split("%")
            day = line[1].split("F")[1]
            month = line[0].split("datepicker=")[1]
            year = line[2].split("&profession")[0][2:6]
            print(year + "-" + month + "-" + day)
        else:
            print("Test Failed")

    def fill_full_name(self):
        # Fill first name and last name
        first_name_field = driver.find_element(By.XPATH, "//input[@name='firstname']")
        last_name_field = driver.find_element(By.XPATH, "//input[@name='lastname']")
        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)

    def fill_drop_down(self):
        # Fill Dropdown
        my_continent = Select(driver.find_element(By.ID, "continents"))
        my_continent.select_by_value(continent)

    def fill_automation_tool(self):
        # Fill Automation Tool
        qTp = driver.find_element(By.XPATH, "//input[@id='tool-0']")
        selenium_IDE = driver.find_element(By.XPATH, "//input[@id='tool-1']")
        selenium_web_driver = driver.find_element(By.XPATH, "//input[@id='tool-2']")
        qTp.click()
        selenium_IDE.click()
        selenium_web_driver.click()

    def fill_profession(self):
        # Fill profession:
        manual_tester = driver.find_element(By.XPATH, "//input[@id='profession-0']")
        automation_tester = driver.find_element(By.XPATH, "//input[@id='profession-1']")
        manual_tester.click()
        automation_tester.click()

    def fill_selenium_commands(self):
        # Fill Selenium Commands:
        my_commands = Select(driver.find_element(By.ID, "selenium_commands"))
        my_commands.select_by_visible_text(command)

    def fill_year_of_experience(self):
        # Fill year of Experience:
        radio = driver.find_element(By.XPATH, "//input[@id='exp-4']")
        radio.click()

    def file_upload(self):
        # File Upload
        browse = driver.find_element(By.XPATH, "//input[@id='photo']")
        browse.send_keys("C:/Automation/Python/test_automation/selenium_automation/lesson02/naruto.png")

    def submit_button(self):
        button = driver.find_element(By.XPATH, "//button[@id='submit']")
        button.click()

    def fill_date(self):
        date_picker = driver.find_element(By.XPATH, "//input[@id='datepicker']")
        date_picker.click()
        data_widget = driver.find_element(By.XPATH, "//div[@id='ui-datepicker-div']")
        cells = data_widget.find_elements(By.TAG_NAME, "td")
        for cell in cells:
            if (cell.text == "19"):
                cell.click()
                break
