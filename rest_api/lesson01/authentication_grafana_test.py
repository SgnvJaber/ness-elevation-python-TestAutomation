import json
import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:3000/"
extend_link = "api/teams/search"


class Test_Grafana_Login:
    def test_print_teams(self):
        response = requests.get(url + extend_link, auth=HTTPBasicAuth('admin', 'admin'))
        result = response.json()
        print(json.dumps(result, indent=2))
