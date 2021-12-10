from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


class Test_Web_Driver_Object_Methods_03:
    def setup_class(cls):
        global driver

    def test_drivers(self):
        #Chrome
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.google.com/")
        driver.quit()
        #Edge
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        driver.get("https://www.google.com/")
        driver.quit()
        #FireFox
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("https://www.google.com/")
        driver.quit()
        #Opera
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        driver.get("https://www.google.com/")
        driver.quit()
