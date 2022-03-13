import requests
import bs4
import time
import urllib.request

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

# os.mkdir('./images')

print(img_url.split('/')[-1])
r = requests.get(img_url)
time.sleep(3)
img_file = open('./images/' + img_url.split('/')[-1], mode='wb')
img_file.write(r.content)
img_file.close()

# for image_data in img_url:
#     r = requests.get(image_data)
#     img_file = open('./images/'+img_url.split('/')[-1], mode='wb')
#     img_file.write(r.content)
#     img_file.close()
