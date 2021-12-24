import csv

import allure
from selenium.webdriver.common.by import By


class Work_Shifts():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get Table Header")
    def get_headers(self):
        return self.driver.find_elements(By.XPATH, "//tr/th[contains(@style,'width')]")

    @allure.step("Get Password field Element")
    def get_rows(self):
        return self.driver.find_elements(By.XPATH, "//tr/td[@class='left']")

    @allure.step("Calling a generic function that takes xpath as in input that returns a list")
    def get_text_from_list(self, elements):
        list = []
        for elem in elements:
            list.append(elem.text)
        return list

    @allure.step("Sign in Flow:")
    def action_export_table_to_CSV(self):
        # open the file in the write mode
        with open('data.csv', 'w', newline='') as f:
            # create the csv writer
            writer = csv.writer(f)
            # write a data to the csv file
            headers = self.get_text_from_list(self.get_headers())
            rows = self.get_text_from_list(self.get_rows())
            writer.writerow(headers)
            list = []
            print(rows)
            for i in range(len(rows)):
                list.append(rows[i] + " ")
                if (i + 1) % len(headers) == 0:
                    writer.writerow(list)
                    list.clear()
