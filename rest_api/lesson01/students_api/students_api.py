import json

import allure
import requests

url = 'http://localhost:9000/student'
header = {'Content-type': 'application/json'}
id = '/90'


class Test_Students_API:

    @allure.title("Verify GET request")
    @allure.description("This test verify that GET request returns a list of students")
    def test_get_students(self):
        response = requests.get(url + "/list")
        result = response.json()
        for student in result:
            print(student["firstName"] + " " + student["lastName"])
        assert response.status_code == 200

    def test_no_courses_POST(self):
        payload = {'firstName': 'Yoni', 'lastName': 'Flenner', 'email': 'yoni2@flenner.com',
                   'programme': 'Some Engineering'}
        response = requests.post(url, json=payload, headers=header)
        result = response.json()
        print(result)
        assert response.status_code == 201

    def test_with_courses_POST(self):
        courses = ["Selenium", "Appium", "Rest API"]
        headers = {'Content-type': 'application/json'}
        payload = {'firstName': 'Yoni', 'lastName': 'Flenner', 'email': 'yoni1@flenner.com',
                   'programme': 'Some Engineering', 'courses': courses}
        response = requests.post(url, json=payload, headers=headers)
        result = response.json()
        print(result)
        assert response.status_code == 201

    def test_put_students(self):
        payload = {'firstName': 'Yoni', 'lastName': 'Flenner', 'email': 'yoni@flenner.com',
                   'programme': 'Physics'}
        response = requests.put(url + id, json=payload, headers=header)
        result = response.json()
        print(result)
        assert response.status_code == 200

    def test_delete_students(self):
        response = requests.delete(url + id)
        print(response)
        assert response.status_code == 204
