# Crawler for Book covers
# Aladin - https://www.aladin.co.kr/

from bs4 import BeautifulSoup
import requests
import re # for file name


# Pages
#url = 'https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&KeyWord=%EC%9D%B4%EB%AC%98%EC%8B%A0&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=11&CustReviewCount=0&CustReviewRank=0&KeyFullWord=%EC%9D%B4%EB%AC%98%EC%8B%A0&KeyLastWord=%EC%9D%B4%EB%AC%98%EC%8B%A0&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&chkKeyISBN=&chkKeyTag=&chkKeyTOC=&chkKeySubject=&ViewRowCount=25&page=1'
url = 'https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&KeyWord=%EC%9D%B4%EB%AC%98%EC%8B%A0&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=11&CustReviewCount=0&CustReviewRank=0&KeyFullWord=%EC%9D%B4%EB%AC%98%EC%8B%A0&KeyLastWord=%EC%9D%B4%EB%AC%98%EC%8B%A0&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&chkKeyISBN=&chkKeyTag=&chkKeyTOC=&chkKeySubject=&ViewRowCount=25&page=2'

# Data requests
req = requests.get(url)
req.status_code

req.text
html = req.content

# Data analysis
soup = BeautifulSoup(html, 'html.parser')

# for Pics
lst_cover = soup.find_all("img", class_ = "i_cover")
for n, i in enumerate(lst_cover):
    lst_cover[n] = i['src'].replace('cover150', 'cover500')

# for Titles
lst_title = soup.find_all('a', class_ = "bo3")
for n, i in enumerate(lst_title):
    tit = i.string
    filename = re.sub('[\/:*?"<>|]','', tit)
    lst_title[n] = filename

# Download
import urllib.request
for m, j in enumerate(lst_cover):
    urllib.request.urlretrieve(j, lst_title[m]+".jpg")

