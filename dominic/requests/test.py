import requests


payload = {'sensor': 'value1', 'value': 'value2'}
r = requests.get('http://192.168.31.12/data', params=payload)
print(r.json())