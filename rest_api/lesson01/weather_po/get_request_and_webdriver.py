import json
import allure
import requests
from selenium import webdriver
from smart_assertions import soft_assert, verify_expectations
from webdriver_manager.chrome import ChromeDriverManager

from rest_api.lesson01.weather_po.weather_page import Weather_Page

url = "http://api.openweathermap.org/data/2.5/weather"
city = "Jerusalem,Il"
key = "ad48510a9aed1ff96b51557d94bc5964"


class Test_Get_Request_And_Webdriver:
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    wp = Weather_Page(driver)

    def setup_class(cls):
        driver.maximize_window()
        driver.get("https://openweathermap.org/")
        driver.implicitly_wait(10)

    # def teardown_class(cls):
    #     driver.quit()

    @allure.step("Get Response")
    def get_response(self, params):
        # Send Request to Server
        params = dict(appid=key, q=city, units='metric')
        response = requests.get(url, params)
        return response

    @allure.title("Verify Request")
    @allure.description("This test Verify request")
    def test_verify(self):
        # Send Request to Server
        params = dict(appid=key, q=city, units='metric')
        response = self.get_response(params)
        result = response.json()
        humidty_api = result["main"]["humidity"]
        humidy_selenium = self.wp.action_get_humidity(city)
        print("")
        print(humidty_api)
        print(humidy_selenium)

        # Verify
        soft_assert(result['sys']['country'] == "IL")
        soft_assert(str(humidty_api) == humidy_selenium)
        verify_expectations()
