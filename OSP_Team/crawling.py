import requests
from bs4 import BeautifulSoup

kakao_url = "https://careers.kakao.com/jobs"
naver_url = "https://recruit.navercorp.com/cnts/tech"
for i in range(0, 7):
    req = requests.get(kakao_url, params={'part': 'TECHNOLOG', 'page': i})
    soup = BeautifulSoup(req.text, 'html.parser')
url = 'https://recruit.navercorp.com/rcrt/list.do?annoId=&sw=&subJobCdArr=1010001%2C1010002%2C1010003%2C1010004%2C1010005%2C1010006%2C1010007%2C1010008%2C1020001%2C1030001%2C1030002%2C1040001%2C1050001%2C1050002&sysCompanyCdArr=&empTypeCdArr=&entTypeCdArr=&workAreaCdArr='
#url = 'https://careers.kakao.com/jobs?part=TECHNOLOGY&keyword=&skilset=&page=1'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

list_area = soup.find_all('li', class_='card_item')
res_dic = {}
link_dic = {}
for job in list_area:
    link = url + job.a["href"]
    title = job.find_all('h4', class_='card_title')
    for text in title:
        title_text = text.get_text()
    tag = job.find_all('dd', class_='info_text')
    tags = []
    for item in tag:
        tags.append(item.get_text().strip())

    res_dic[title_text] = tags
    link_dic[title_text] = link

#print(res_dic)
print(link_dic)