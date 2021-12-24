import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BookStore_Page():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get Books Elements as a List")
    def get_books_element_list(self):
        return self.driver.find_elements(By.XPATH, "//li/a/h2")

    @allure.step("Get Displayed Books Titles Elements")
    def get_displayed_books_titles(self):
        return self.driver.find_elements(By.XPATH, "//li[not(contains(@class,'ui-screen-hidden'))]/a/h2")

    @allure.step("Get Displayed Books Prices Elements")
    def get_displayed_books_prices(self):
        return self.driver.find_elements(By.XPATH,
                                         "//li[not(contains(@class,'ui-screen-hidden'))]/a/p[contains(@id,'price')]")

    @allure.step("Get First Book Element")
    def get_first_book_title_element(self):
        return self.driver.find_element(By.XPATH, "//li[@class='ui-li-has-thumb ui-first-child']/a/h2")

    @allure.step("Get Last Book Element")
    def get_last_book_title_element(self):
        return self.driver.find_element(By.XPATH, "//li[@class='ui-li-has-thumb ui-last-child']/a/h2")

    @allure.step("Get search Element")
    def get_searchbar_element(self):
        return self.driver.find_element(By.XPATH, "//input[@id='searchBar']")

    @allure.step("Get Books Size:")
    def action_get_books_size(self):
        return len(self.get_books_element_list())

    @allure.step("Get the number of books with given keyword:")
    def action_get_books_with_keyword_size(self, keyword):
        self.get_searchbar_element().send_keys(keyword)
        self.get_searchbar_element().send_keys(Keys.ENTER)
        time.sleep(1)
        return len(self.get_displayed_books_titles())

    @allure.step("Get title of the first and last book:")
    def action_print_first_and_last_book_titles(self):
        first_book_title = self.get_first_book_title_element().text
        last_book_title = self.get_last_book_title_element().text
        print("First Book:" + first_book_title + " " + " Last Book:" + last_book_title)

    @allure.step("Get Books as Dictionary")
    def action_get_books_dictionary(self):
        dict = {}
        titles = self.get_displayed_books_titles()
        prices = self.get_displayed_books_prices()
        for i in range(len(titles)):
            dict[titles[i].text] = float(prices[i].text[1:])
        return dict

    @allure.step("Print Books List From Low to high")
    def action_get_books_dict_from_low_to_high(self):
        books_dict = self.action_get_books_dictionary()
        sorted_books = dict(sorted(books_dict.items(), key=lambda item: item[1], reverse=False))
        return sorted_books

    @allure.step("Print Books from low to high")
    def action_print_books_from_low_to_high(self):
        books_dict = self.action_get_books_dict_from_low_to_high()
        for book in books_dict:
            print("Title: " + book + " Price: " + str(books_dict[book]))
