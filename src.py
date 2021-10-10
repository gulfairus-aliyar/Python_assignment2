from bs4 import BeautifulSoup  # pip install beautifulsoup4
import requests  # pip install requests

# Load the webpage content
html_text = requests.get('https://coinmarketcap.com/currencies/ethereum/news/').text

# Convert to a beautiful soup object
soup = BeautifulSoup(html_text, 'lxml')


def getDate_byReq(curName):
    someList = []
    for paragraph in soup.find_all('p'):
        if curName in paragraph.get_text():
            someList.append(paragraph.get_text())
    return someList


def get_Data(someList=None):
    someList = []
    for paragraph in soup.find_all('p'):
        someList.append(paragraph.get_text())
    return someList
