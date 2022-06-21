import requests
from bs4 import BeautifulSoup

url = "https://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10016&BizJobtype_Bctgr_Name=IT%C2%B7%EC%9D%B8%ED%84%B0%EB%84%B7&BizJobtype_Code=0&BizJobtype_Name=IT%C2%B7%EC%9D%B8%ED%84%B0%EB%84%B7+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%ED%95%99%EB%A0%A5+%EC%A0%84%EC%B2%B4&MidScroll=0"
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
list_area = soup.find('ol', class_="rankList")

# key가 회사 이름, value.0은 공고 제목 value.1은 상세 링크
res_dic = {}
# key가 회사 이름, values는 태그 리스트
tags_dic = {}

for job in list_area.find_all('li'):
    # 회사 이름
    company_data = job.find('div', class_="coTit")
    company = company_data.find('b').text

    # 공고 제목 과 세부 페이지 링크
    info_data = job.find('div', class_="tit").find('a')
    title = info_data.find('span').text
    link = "https://www.jobkorea.co.kr" + info_data['href']

    # 태그 정보
    tags_data = job.find('div', class_='sTit').find_all('span')
    tags = []
    for tag in tags_data:
        tags.append(tag.text)

    res_dic[company] = [title, link]
    tags_dic[company] = tags

print(res_dic)
print(tags_dic)



