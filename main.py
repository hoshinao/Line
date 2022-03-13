import os
import requests
import glob
import get_gazi

import requests
import bs4
import time
import urllib.request
import os
import shutil


images_update = get_gazi.call_today_covid19()


path = os.listdir('./images/')
print(path[0])
#画像送信
TOKEN = 'hIKKKs4H0hkZlGsGaMEeBcCWdQ2h5gluvu8tImlsBSO'
message = "本日のコロナ感染者数"
image_file = 'C:/Users/programing/PycharmProjects/Line/images/'+path[0]
binary = open(image_file, mode="rb")
image_dic = {"imageFile": binary}
api_url = 'https://notify-api.line.m' \
          'e/api/notify'
headers = {'Authorization': 'Bearer' + " " + TOKEN}
data = {'message': message}
requests.post(api_url, headers=headers, data=data, files=image_dic)
