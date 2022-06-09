import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

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
            url = "https://careers.kakao.com/jobs"
            req = requests.get(url)
            soup = BeautifulSoup(req.text, 'html.parser')

            list_area = soup.find_all('div', class_='wrap_info')
            res_dic = {}
            link_dic = {}
            for job in list_area:
                link = "https://careers.kakao.com" + job.a["href"]
                title = job.find_all('h4', class_='tit_jobs')
                for text in title:
                    title_text = text.get_text()
                tag = job.find_all('a', class_='link_tag')
                tags = []
                for item in tag:
                    tags.append(item.get_text().strip())

                res_dic[title_text] = tags
                link_dic[title_text] = link

            return render_template('kakao.html', result=res_dic, link=link_dic)

        # if (company.__eq__("naver")):
        #     url = "https://recruit.navercorp.com/rcrt/list.do?annoId=&sw=&subJobCdArr=1010001%2C1010002%2C1010003%2C1010004%2C1010005%2C1010006%2C1010007%2C1010008%2C1020001%2C1030001%2C1030002%2C1040001%2C1050001%2C1050002&sysCompanyCdArr=&empTypeCdArr=&entTypeCdArr=&workAreaCdArr="
        #     req = requests.get(url)
        #     soup = BeautifulSoup(req.text, 'html.parser')
        #
        #     return render_template('naver.html')

if __name__=='__main__':
    app.run()