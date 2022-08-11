import requests

from bs4 import BeautifulSoup

# url = 'https://en.wikipedia.org/wiki/Assassination_of_John_F._Kennedy'
url = 'https://en.wikipedia.org/wiki/History_of_Bali'


def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    list_results = soup.findAll("a", attrs={"title": "Wikipedia:Citation needed"})
    print("Citations needed: ", len(list_results))


def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    list_results = soup.findAll("a", attrs={"title": "Wikipedia:Citation needed"})
    for item in list_results:
        print(item.parent.parent.parent.text)


get_citations_needed_count(url)

get_citations_needed_report(url)