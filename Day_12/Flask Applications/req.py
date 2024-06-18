import requests


payload = dict(nm='value1',)
r = requests.post('http://127.0.0.1:5000/login', data=payload)
print(r.text)
