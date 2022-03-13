import re
import write
import bs4
import requests
import datetime
import pytz
from bs4 import BeautifulSoup
from pygments.lexers import r
import os
#os.mkdir('./images')

URL = 'https://www.city.obihiro.hokkaido.jp/covid19/1006986/1007505.html'

req = requests.get(URL)
data = bs4.BeautifulSoup(req.content, 'html.parser')
img_tag = data.find_all('img')
#print(img_tag[4])
data_url = img_tag[4]['src']
root_url = "https://www.city.obihiro.hokkaido.jp"
img_url = root_url + data_url
print(f"url＝{img_url}")
for image_data in img_url:
    r = requests.get(image_data)
    img_file = open('./images/'+img_url.split('/')[-1], mode='wb')
    img_file.write(r.content)
    img_file.close()

# from PIL import Image
# import io
#
# io_byte = io.BytesIO(requests.get(img_url).content)
# print(io_byte)
# #print(requests.get(io_byte).content)


# soup = BeautifulSoup(response.text, 'html.parser')
# image_file = './gazo.png'
# binary = open(image_file, mode='rb')
# image_dic = {'imageFile': binary}
#
# time = datetime.datetime.now(pytz.timezone("Asia/Tokyo"))
# time = time.strftime('%Y年%m月%d日 %H:%M:%S')
#
# TOKEN = 'Ty71KIoTUVVomIrKdHnHasNcs5VJHvale74Zw8h0cQ6'
#
# api_url = 'https://notify-api.line.me/api/notify'
#
# send_contents = time
#
# TOKEN_dic = {'Authorization': 'Bearer' + " " + TOKEN}
# send_dic = {'message': send_contents}

#requests.post(api_url, headers=TOKEN_dic, data=send_dic, files=image_dic)
