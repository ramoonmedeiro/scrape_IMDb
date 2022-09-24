import scrape
from bs4 import BeautifulSoup
import requests

url = 'https://www.imdb.com/chart/top/'

info = list()
info_geral = list()

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

for i in range(0, 250, 1):
	ano = scrape.years(soup)[i].text.replace(')', '').replace('(', '')
	filme = scrape.films(soup)[i].find('a').text
	nota_imdb = scrape.imdb(soup)[i].text

	info.append(ano) 
	info.append(filme)
	info.append(nota_imdb)
	info_geral.append(info)
	info = []

scrape.create_db(info_geral)