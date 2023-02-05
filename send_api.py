import requests
import json

url = 'http://127.0.0.1:8000/login'

params = {
    'username' : '123',
    'password' : '456'
}

html = requests.post(f'{url}', json.dumps(params))