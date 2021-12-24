from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector


class Test_DB:

    def setup_class(cls):
        global driver
        global mydb
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/demo/")
        driver.implicitly_wait(5)

        mydb = mysql.connector.connect(
            host="remotemysql.com",
            database='HgcKGz4q8T',
            user="HgcKGz4q8T",
            password="x0MLwiZ7im"
        )

    def test_01(self):
        query = "SELECT user_name,password FROM Users WHERE comments ='correct'"
        my_cursor = mydb.cursor()
        my_cursor.execute(query)
        my_result = my_cursor.fetchall()
        driver.find_element_by_name("username").send_keys(my_result[0][0])
        driver.find_element_by_name("password").send_keys(my_result[0][1])
        driver.find_element_by_id("submit").click()

    def teardown_class(cls):
        mydb.close()
        driver.quit()
