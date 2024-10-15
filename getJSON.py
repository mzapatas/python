from pprint import pprint
import requests

url = 'https://randomuser.me/api/?results=1'
users = requests.get(url).json()
pprint(users)