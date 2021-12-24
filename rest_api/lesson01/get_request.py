import json
import allure
import requests
from smart_assertions import soft_assert, verify_expectations

url = "http://api.openweathermap.org/data/2.5/weather"
city = "Jerusalem,Il"
key = "ad48510a9aed1ff96b51557d94bc5964"


class Test_Get_Request:

    @allure.step("Get Response")
    def get_response(self, params):
        # Send Request to Server
        params = dict(appid=key, q=city, units='metric')
        response = requests.get(url, params)
        return response

    @allure.title("Verify Get Request")
    @allure.description("This test Verify get request")
    def test_verify_get_request(self):
        # Send Request to Server
        params = dict(appid=key, q=city, units='metric')
        response = self.get_response(params)

        # Print Response
        result = response.json()
        print(json.dumps(result, indent=2))

        # Print Status Code
        print(response.status_code)

        # part Date
        print("Date: ", response.headers["Date"])

        # Verify
        soft_assert(response.headers['Content-Type'] == 'application/json; charset=utf-8')
        soft_assert(response.status_code == 200)
        verify_expectations()


