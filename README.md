# Final_OSP Team Project
2022_1 오픈소스프로그래밍 9조<br>
*collaborator: 유지예, 송혜경, 최표선, 하재현* 
<br>

## 인턴 채용 정보를 한 곳에!
인턴 채용 공고 조회 사이트 <br>
(Linux Shell Script, Python, Flask 기반 웹서비스)

**담당 파트**
1. Backend - 유지예, 송혜경, 하재현
- Data Crawling
- Elasticsearch data store 
2. FrontEnd - 최표선, 하재현
- main page
- crawling page

**실행 과정**
1. 실행 쉘 스크립트 파일을 실행해 필요한 모듈을 다운받고, app.py가 실행됩니다.
2. 메인 페이지에 들어가면 채용 정보를 확인할 수 있는 6개의 IT기업이 있습니다.
3. 원하는 기업의 로고를 클릭하면 해당 기업 Tech분야의 **취업 공고 제목, 태그, 상세페이지 링크**를 crawling 해옵니다. <br>
   (태그가 존재하지 않는 기업 사이트는 크롤링 정보가 없습니다.)  
4. crawling 정보를 리스트 형식으로 확인할 수 있고, <br>
   제목을 누르면 세부 사이트로 연결해 내용을 확인할 수 있습니다.
5. 되돌아 가는 버튼을 누르면 다시 메인 페이지로 들어갈 수 있습니다.
6. main 페이지에서 추가로 일간 채용 Top10 크롤링 정보를 확인할 수 있고, <br>
   제목을 누르면 세부 사이트로 연결해 내용을 확인할 수 있습니다.

**유의 사항**
- selenium 기반 웹크롤링을 위해서는 chrome webdriver version이 사용자의 chrome version과 맞아야 하기 때문에 쉘 파일을 실행해도 본인의 버전과 일치하지 않으면 크롤링이 제대로 이루어 지지 않을 수도 있습니다. (version 102.0.5005.61 으로 진행)
- app.py가 제대로 실행되지 않은 경우, [잡코리아 사이트](https://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10016&BizJobtype_Bctgr_Name=IT%C2%B7%EC%9D%B8%ED%84%B0%EB%84%B7&BizJobtype_Code=0&BizJobtype_Name=IT%C2%B7%EC%9D%B8%ED%84%B0%EB%84%B7+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%ED%95%99%EB%A0%A5+%EC%A0%84%EC%B2%B4&MidScroll=0)에 들어가 보안코드를 입력하는 과정을 거쳐야 합니다. (사이트 내 보안정책)
- python3가 linux 환경에 깔려있어야 한다.

**시연 영상**

풀영상은 시연영상 파일 내에 있는 구글 드라이브를 확인 하시면 됩니다. <br>
<img src="https://user-images.githubusercontent.com/81686317/174798224-230806b8-610c-41ca-83bd-69daf4ab7250.gif">
