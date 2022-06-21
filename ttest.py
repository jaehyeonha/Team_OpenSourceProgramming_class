import re
import requests
import sys
import pprint
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

# field = ["tech", "design", "service", "client"]
# company = ["c1", "c2", "c3"]
# job_dic = {"c1":["job1", "job2", "job3"], "c2":["job4", "job5"]}

# # index랑 doc_type차이점

# for job in job_dic.keys():
#     print(job)
#     print(job_dic[job])
    
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

def insert(body):
    return es.index(index=index, doc_type=doc_type, body=body)
    
def search(index, data=None):
    if data is None:
        data = {"match_all": {}}
    else:
        data = {"match": data}
    
    body = {"query": data}
    res = es.search(index=index, body=body)
    return res

index = 'employment'
doc_type = 'kakao'
data ={
    'title': '',
    'tags': '',
    'content': '',
    'url': ''
}

# for job in res_dic.keys():
#     data['title'] = job
#     data['tags'] = res_dic[job]
#     data['url'] = link_dic[job]
#     ir = insert(data)
    
#     print(ir)

sr = search(index)
pprint.pprint(sr)
