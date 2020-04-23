import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
from user import User

url = 'https://www.instagram.com/rodolfo_saldanha/?__a=1'

try:
    response = requests.get(url)
except:
    print('User not available')

userInfo_json = json.loads(response.text)

info = userInfo_json['graphql']['user']
user = User(info['full_name'], info['edge_followed_by']['count'], info['edge_follow']['count'],
               info['business_category_name'], info['is_verified'], info['edge_owner_to_timeline_media']['count'])

print(user.print_info())

exit(1)