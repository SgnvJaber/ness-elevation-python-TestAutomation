import json
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://api.chucknorris.io/jokes/'
expected_get_status_code = 200


class Test_ChuckNorris_Api:
    # part 1
    def test_1_get_categories(self):
        categories_list = 'categories'
        response = requests.get(url + categories_list)
        result = response.json()
        print(json.dumps(result, indent=2))
        assert response.status_code == expected_get_status_code

    # part 2
    def test_2_chuck_norris(self):
        barack_jokes_size = self.get_serach_size('Barack Obama')
        sheen_jokes_size = self.get_serach_size('Barack Obama')
        if (barack_jokes_size > sheen_jokes_size):
            print("Barack has more jokes than Sheen: ")

        elif (barack_jokes_size < sheen_jokes_size):
            print("Sheen has more jokes than Barack: ")
        else:
            print("Equals Number Of Jokes!")

    # part 3
    def test_3_chuck_norris(self):
        value = 'random'
        for x in range(10):
            response = requests.get(url + value)
            result = response.json()
            with open('data.txt', 'w', newline='') as f:
                json.dump(result['value'], f)
                f.write('\n')

    # part 4
    def test_4_chuck_norris(self):
        value = 'random'
        response = requests.get(url + value)
        url_web = str(response.json()['url'])
        value = str(response.json()['value'])
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(url_web)
        driver.implicitly_wait(5)
        try:
            assert driver.find_element_by_xpath("//*[@id='content']/section/blockquote/p").text == value
        except Exception as e:
            print(e)
        finally:
            driver.quit()

    def get_serach_size(self, seach_query):
        search_url = 'search'
        params = dict(query=seach_query)
        response = requests.get(url + search_url, params)
        return response.json()['total']
