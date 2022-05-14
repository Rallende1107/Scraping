from bs4 import BeautifulSoup
import requests
import lxml.html as html
import pandas as pd

url = ('https://myanimelist.net/anime/40356/Tate_no_Yuusha_no_Nariagari_Season_2')
page = requests.get(url)
contenido = page.text

soup = BeautifulSoup(contenido, 'lxml')
print(soup.prettify())

nombre = soup.find("h1", class_="title-name").get_text()
nombre_alterno = soup.find("p", class_="title-english").get_text()
link = soup.find("div", class_="breadcrumb ").get_text()


print(nombre)
print(nombre_alterno)
print(link)
