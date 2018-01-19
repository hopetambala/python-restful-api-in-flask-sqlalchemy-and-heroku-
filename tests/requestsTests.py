
# coding: utf-8

import requests

url = 'http://localhost:5000/person/'

r = requests.get(url)
r = requests.post(url, data = {'fname' : "Hello",'lname': 'lady'})
r = requests.delete(url + "1")

for i in range(100):
    r = requests.delete(url + str(i))



