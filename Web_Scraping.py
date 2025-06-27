import pandas as pd
import requests as r
from bs4 import BeautifulSoup
sourish=r.get('https://chatgpt.com/c/685ebe46-f828-8005-a668-a6d3352e8a33').text
print(sourish)
v=BeautifulSoup(sourish,'html.parser')
y=v.find_all('B','Strong')
adding_a_tag=[]
for i in y:
    print(i.text)