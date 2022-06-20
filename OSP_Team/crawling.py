import re
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

url = "https://career.woowahan.com/?jobCodes&employmentTypeCodes=&serviceSectionCodes=&careerPeriod=&keyword=&category=jobGroupCodes%3ABA005001#recruit-list"
driver = webdriver.Chrome(executable_path = 'C:\\chromedriver_win32\\chromedriver')
driver.get(url)
driver.implicitly_wait(5)

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(0.5)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")

    if new_height == last_height:
        break
    else:
        last_height = new_height

new_height = last_height

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

list_area = soup.find('ul', class_='recruit-type-list')
res_dic = {}
link_dic = {}
for job in list_area.find_all('li', class_=False):
    link = "https://career.woowahan.com/" + job.a["href"]
    title = job.find('p',  class_="fr-view").text
    tag = job.find_all('div', class_='flag-tag')
    tags = []
    for item in tag:
        tags.append(item.get_text().strip())

    res_dic[title] = tags
    link_dic[title] = link

print(link_dic)
print(res_dic)



