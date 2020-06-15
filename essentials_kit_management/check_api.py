import requests

url = f'http://127.0.0.1:8080/api/essentials_kit_management/listofforms/?limit={5}&offset={0}'
headers = {"content-type": "application/json", "Authorization": "Bearer token_meg"}
response = requests.get(url, headers=headers)
print(response.content)
