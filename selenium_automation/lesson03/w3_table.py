import csv

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

expected_row_size = 7
expected_col_size = 3
expected_country_size = 4


class Test_W3_Table:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.w3schools.com/html/html_tables.asp")

    def teardown_class(cls):
        driver.quit()

    @allure.step("Attaching a screenshot to the report")
    def attach_file(self):
        image = "./screen-shots/screen.png"  # need to create folder: screen-shots first
        driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

    @allure.title("Verify Table rows")
    @allure.description("This test verifies that the number of rows is as expected")
    def test_verify_table_rows(self):
        rows = self.get_rows()
        assert len(rows) == expected_row_size

    @allure.title("Verify Table cols")
    @allure.description("This test verifies that the number of cols is as expected")
    def test_verify_table_cols(self):
        headers = self.get_headers()
        assert len(headers) == expected_col_size

    @allure.title("Verify Europe Countries")
    @allure.description("This test verifies that the number of europe countries is as expected")
    def test_verify_europe_countries(self):
        europe_countries = self.get_europe_countries()
        print(europe_countries)
        assert len(europe_countries) == expected_country_size

    @allure.title("Generate CSV File")
    @allure.description("Exporting the table into a CSV file")
    def test_write_to_csv(self):
        self.generate_csv()

    @allure.step("Getting list of countries")
    def get_countries(self):
        return self.get_text_from_list("//*[@id='customers']/tbody/tr/td[3]")

    @allure.step("Getting list of contacts")
    def get_contacts(self):
        return self.get_text_from_list("//*[@id='customers']/tbody/tr/td[2]")

    @allure.step("Getting list of companies")
    def get_companies(self):
        return self.get_text_from_list("//*[@id='customers']/tbody/tr/td[1]")

    @allure.step("Calling a generic function that takes xpath as in input that returns a list")
    def get_text_from_list(self, xpath):
        elements = driver.find_elements(By.XPATH, xpath)
        list = []
        for elem in elements:
            list.append(elem.text)
        return list

    @allure.step("Getting list of Eurpoe Countries")
    def get_europe_countries(self):
        europe_countries = self.get_countries()
        europe_countries.remove("Mexico")
        europe_countries.remove("Canada")
        return europe_countries

    @allure.step("Getting the table rows")
    def get_rows(self):
        rows = self.get_text_from_list("//table[@id='customers']/tbody/tr")
        return rows

    @allure.step("Getting the table headers")
    def get_headers(self):
        headers = self.get_text_from_list("//table[@id='customers']/tbody/tr/th")
        return headers

    @allure.step("A function to generate a CSV file from the table")
    def generate_csv(self):
        # open the file in the write mode
        with open('data.csv', 'w', newline='') as f:
            # create the csv writer
            writer = csv.writer(f)
            # write a data to the csv file
            headers = self.get_headers()
            companies = self.get_companies()
            contacts = self.get_contacts()
            countries = self.get_countries()
            writer.writerow(headers)
            list = []
            for i in range(len(countries)):
                list.append(companies[i])
                list.append(contacts[i])
                list.append(countries[i])
                writer.writerow(list)
                list.clear()
