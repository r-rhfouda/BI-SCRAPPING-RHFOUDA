import requests as rq
from bs4 import BeautifulSoup as bs
# User-Agent header
url = "https://github.com/search?q=mental+health"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
page = rq.get(url, headers=headers)
#Check request successful (Status 200)
if page.status_code==200:
    #Parse the HTML
    soup = bs(page.text, 'html.parser')
    #All links (<a> tags)
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))
else:
    print(f"Failed to load page. Status code: {page.status_code}")
