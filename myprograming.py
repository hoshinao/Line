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

URL = 'https://www.city.obihiro.hokkaido.jp/covid19/1006986/1007505.html'
header_dic = {"User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46"}

# response = urllib.request.Request(url = URL,headers=header_dic)
# print(response)

req = requests.get(URL)
data = bs4.BeautifulSoup(req.content, 'html.parser')
img_tag = data.find_all('img')
print(img_tag[4])
data_url = img_tag[4]['src']
data_urls = data_url[4:86]
root_url = "https://www.city.obihiro.hokkaido.jp"
img_url = root_url + data_urls
print(f"url＝{img_url}")

print(img_url.split('/')[-1])

shutil.rmtree('images')
os.mkdir('images')

r = requests.get(img_url)
time.sleep(3)
img_file = open('C:/Users/programing/PycharmProjects/Line/images/' + img_url.split('/')[-1], mode='wb')
img_file.write(r.content)
img_file.close()

path = os.listdir('C:/Users/programing/PycharmProjects/Line/images/')
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
