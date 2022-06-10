import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

kakao_url = "https://careers.kakao.com/jobs"
res_dic = {}
link_dic = {}
for i in range(1, 7):
    url = kakao_url + "?page=" + str(i)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    list_area = soup.find_all('div', class_='wrap_info')
    for job in list_area:
        link = "https://careers.kakao.com" + job.a["href"]
        title = job.find('h4', class_='tit_jobs').text

        tag = job.find_all('a', class_='link_tag')
        tags = []
    for item in tag:
        tags.append(item.get_text().strip())

        res_dic[title] = tags
        link_dic[title] = link

print(res_dic)
print(link_dic)
# last_height = driver.execute_script("return document.body.scrollHeight")
#
# while True:
#     scroll_down = 0
#     while scroll_down < 10:
#         elem.send_keys(Keys.PAGE_DOWN)
#         time.sleep(0.2)
#         scroll_down += 1
#
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         list_area = soup.find_all('li', class_='card_item')
#         res_dic = {}
#         link_dic = {}
#         for job in list_area:
#             link = url + job.a["href"]
#             title = job.find_all('h4', class_='card_title')
#             for text in title:
#                 title_text = text.get_text()
#             tag = job.find_all('dd', class_='info_text')
#             tags = []
#             for item in tag:
#                 tags.append(item.get_text().strip())
#
#             res_dic[title_text] = tags
#             link_dic[title_text] = link
#         break
#
#     last_height = new_height








