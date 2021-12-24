import allure
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from smart_assertions import soft_assert, verify_expectations
from webdriver_manager.chrome import ChromeDriverManager

from python_exam.ex1_po.bookstore_page import BookStore_Page
from python_exam.test_listeners import EventListener

expected_total_books = 8
keyword = "Java"


class Test_Main_Page:
    global driver
    edriver = webdriver.Chrome(ChromeDriverManager().install())
    driver = EventFiringWebDriver(edriver, EventListener())
    books = BookStore_Page(driver)

    def setup_class(cls):
        driver.maximize_window()
        driver.get("https://automationbookstore.dev")
        driver.implicitly_wait(2)

    def teardown_class(cls):
        driver.quit()

    @allure.title("Verify Number of Books")
    @allure.step("This test verify that the number of books is as expected")
    def test_1_verify_books_size(self):
        assert self.books.action_get_books_size() == expected_total_books

    @allure.title("Verify Books with given keyword")
    @allure.step("This test verify that the number of books  with given keyword is less than the total books")
    def test_2_verify_books_with_keyword(self):
        assert self.books.action_get_books_with_keyword_size(keyword) < expected_total_books

    @allure.title("Print First And Last Book Name")
    @allure.step("This test print the title of the first and last book")
    def test_3_print_first_and_last_book_titles(self):
        # self.books.action_get_books_with_keyword_size(keyword) apply filter
        self.books.action_print_first_and_last_book_titles()

    @allure.title("Print list of Books With Prices from low to High")
    @allure.step("This test verify the books are printed from low to high")
    def test_4_print_list_of_books_low_to_high(self):
        self.books.action_print_books_from_low_to_high()
        books_dict = self.books.action_get_books_dict_from_low_to_high()
        prices = list(books_dict.values())
        # Verify results
        current_price = prices[0]
        #  pip install smart-assertions
        for next_price in prices:
            soft_assert(current_price <= next_price)
        verify_expectations()
