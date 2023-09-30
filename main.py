import requests
import string
from bs4 import BeautifulSoup

Search_input = input("Search :- ")
cap_seach = string.capwords(Search_input)
lists = cap_seach.split()
word = "_".join(lists)