#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("main.html")

@app.route('/contents', methods=['POST'])
def contents():
    error = None
    if request.method == 'POST':
        company = request.form['company']

        if (company.__eq__("kakao")):
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

            return render_template('kakao.html', result=res_dic, link=link_dic)

        if (company.__eq__("naver")):
            url = "https://recruit.navercorp.com/rcrt/list.do?srchClassCd=1000000"
            driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
            driver.get(url)
            driver.implicitly_wait(5)

            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
                time.sleep(0.1)
                new_height = driver.execute_script("return document.documentElement.scrollHeight")

                if new_height == last_height:
                    break
                else:
                    last_height = new_height

            new_height = last_height

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            list_area = soup.find_all('li', class_='card_item')
            res_dic = {}
            link_dic = {}
            for job in list_area:
                show = job.a["onclick"]
                show_number = re.sub(r'[^0-9]', '', show)
                link = "https://recruit.navercorp.com/rcrt/view.do?annoId=" + show_number + "&sw=&subJobCdArr=1010001%2C1010002%2C1010003%2C1010004%2C1010005%2C1010006%2C1010007%2C1010008%2C1020001%2C1030001%2C1030002%2C1040001%2C1050001%2C1050002%2C1060001&sysCompanyCdArr=&empTypeCdArr=&entTypeCdArr=&workAreaCdArr="
                title = job.find('h4', class_='card_title').text
                tag = job.find_all('dd', class_='info_text')
                tags = []
                for item in tag:
                    tags.append(item.get_text().strip())

                res_dic[title] = tags
                link_dic[title] = link

            return render_template('naver.html', result=res_dic, link=link_dic)

        if (company.__eq__("line")):
            url = "https://careers.linecorp.com/jobs?ca=Engineering"

            req = requests.get(url)
            soup = BeautifulSoup(req.text, 'html.parser')

            res_dic = {}
            link_dic = {}

            for job in soup.find('ul', class_="job_list").find_all('li'):
                link = "https://careers.linecorp.com/" + job.find('a')["href"]
                title = job.find('h3', class_='title').text
                tag = job.find_all('div', class_='text_filter')
                tags = []
                for item in tag:
                    tags.append(item.get_text().strip())

                res_dic[title] = tags
                link_dic[title] = link

            return render_template('line.html', result=res_dic, link=link_dic)

        if (company.__eq__("coupang")):
            url = 'https://www.coupang.jobs/kr/jobs/?department=Ecommerce+Engineering&department=Play+Engineering&department=Product+UX&department=Search+and+Discovery&department=Search+and+Discovery+Core+Infrastructure&department=Cloud+Platform&department=Corporate+IT&department=eCommerce+Product&department=FTS+(Fulfillment+and+Transportation+System)&department=Marketplace%2c+Catalog+%26+Pricing+Systems&department=Program+Management+Office&department=Customer+Experience+Product'
            req = requests.get(url)
            soup = BeautifulSoup(req.text, 'html.parser')

            list_area = soup.find_all('div', class_='card-body')
            link_dic = {}

            for job in list_area:
                link = "https://www.coupang.jobs" + job.a["href"]
                title = job.find_all('a', class_='stretched-link')
                for text in title:
                    title_text = text.get_text(

                    )

                link_dic[title_text] = link

            return render_template('coupang.html', link=link_dic)

if __name__=='__main__':
    app.run()