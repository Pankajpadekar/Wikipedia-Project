import requests
import string
from bs4 import BeautifulSoup

Search_input = input("Search :- ")
cap_seach = string.capwords(Search_input)
lists = cap_seach.split()
word = "_".join(lists)

url ="https://n.wikipedia.org/wiki/"+word

def wikiSearch(url):
    url_link =requests.get(url)
    soup = BeautifulSoup(url_link.content, 'html.parser')
    details_info = soup('table' , {'class':'infobox'})
    for i in details_info: