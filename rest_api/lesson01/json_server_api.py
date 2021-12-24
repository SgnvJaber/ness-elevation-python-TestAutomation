import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = 'http://localhost:3000'
resource = '/posts'
id = '/101'


class Test_API_Requests:
    # POST request
    def test_post_request(self):
        payload = {"userId": 11, "id": "101", "title": "test", "body": "123"}
        response = requests.post(url + resource, data=payload)
        result = response.json()
        print('~~~~~~~~~~~~~~~~~\n', result)
        assert response.status_code == 201

        expected = '101'
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(1)
        try:
            assert driver.find_element_by_xpath("//a[@href='posts']/following-sibling::sup").text == expected + 'x'
            # or another option:
            # self.verify_number_of_items('posts', 101)
        except Exception as e:
            print(e)
        finally:
            driver.quit()

    # PUT request
    def test_put_request(self):
        payload = {"userId": 11, "id": 101, "title": "Yoni", "body": "456"}
        response = requests.put(url + resource + id, data=payload)
        result = response.json()
        print('~~~~~~~~~~~~~~~~~\n', result)
        assert response.status_code == 200

    # PATCH request
    def test_patch_request(self):
        payload = {"title": "Kuku"}
        response = requests.patch(url + resource + id, data=payload)
        result = response.json()
        print('~~~~~~~~~~~~~~~~~\n', result)
        assert response.status_code == 200

    # DELETE request
    def test_delete_request(self):
        response = requests.delete(url + resource + id)
        result = response.json()
        print('~~~~~~~~~~~~~~~~~\n', result)
        assert response.status_code == 200

        expected = '100'
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(1)
        try:
            assert driver.find_element_by_xpath("//a[@href='posts']/following-sibling::sup").text == expected + "x"
            # or another option:
            # self.verify_number_of_items('posts', 100)
        except Exception as e:
            print(e)
        finally:
            driver.quit()

    def verify_number_of_items(self, resource_name, expected_result):
        actual_result = driver.find_element_by_xpath("//a[@href='" + resource_name + "']/following-sibling::sup").text
        assert int(actual_result[
                   :-1]) == expected_result  # actual_result = removes the last character (x) and convert it to int

    def test_options(self):
        # options provides us additional data coming from the server, for example the allow property represents the methods wich are supported in this service like: GET / POST / OPTIONS...
        # most services do not sopport options
        response = requests.get('https://httpbin.org/get')
        opt = requests.options(response.url)
        print('\nSupported Methods:', opt.headers['allow'])
