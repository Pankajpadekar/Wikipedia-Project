import requests
import string
from bs4 import BeautifulSoup

# Website = "https://en.wikipedia.org/wiki/"

while True:
    Search_input = input("Search :- ")
    cap_seach = string.capwords(Search_input)
    lists = cap_seach.split()
    word = "_".join(lists)

    url ="https://en.wikipedia.org/wiki/"+ word


    def wikiSearch(url):
        url_link = requests.get(url)
        soup = BeautifulSoup(url_link.content, 'html.parser')
        details_info = soup('table' , {'class':'infobox'})
        for i in details_info:
            h = i.find_all('tr')
            for j in h:
                heading = j.find_all('th')
                detail = j.find_all('td')
                if heading is not None and detail is not None:
                    for x,y in zip(heading,detail):
                        print(f"{x.text} :: {y.text}")
                        print("------------------")

        for i in range(1,10):
            print(soup('p')[i].text)

    wikiSearch(url)
