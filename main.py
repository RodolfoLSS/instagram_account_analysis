import requests
import time
from bs4 import BeautifulSoup
import json
from user import User
from photo import Photo
from video import Video

profile = 'https://www.instagram.com/cristiano/?__a=1'

try:
    response = requests.get(profile)
except:
    print('User not available')

userInfo_json = json.loads(response.text)

info = userInfo_json['graphql']['user']
user = User(info['full_name'], info['edge_followed_by']['count'], info['edge_follow']['count'],
               info['business_category_name'], info['is_verified'], info['edge_owner_to_timeline_media']['count'])

for media in info['edge_owner_to_timeline_media']['edges']:
    node = media['node']

    if(node['is_video']):
        video = Video(node['edge_media_to_caption']['edges'][0]['node']['text'], node['edge_media_to_comment']['count'],
                      node['edge_liked_by']['count'], node['accessibility_caption'])
        user.videos.append(video)
    else:
        photo = Photo(node['edge_media_to_caption']['edges'][0]['node']['text'], node['edge_media_to_comment']['count'],
                      node['edge_liked_by']['count'], node['accessibility_caption'])
        user.photos.append(photo)

user.calculate_photo_averages()
user.calculate_videos_averages()
user.calculate_media_averages()

print(user.print_info())

exit(1)