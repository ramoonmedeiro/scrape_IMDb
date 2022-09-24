import pandas as pd
import numpy as np
import json
import sqlite3

def years(soup):

	anos = soup.find_all('span', {'class':'secondaryInfo'})
	return anos

def films(soup):

	filmes = soup.find_all('td', {'class':'titleColumn'})
	return filmes

def imdb(soup):

	notas = soup.find_all('strong')
	return notas

def create_db(lista):
	lista = np.array(lista)
	df = pd.DataFrame(lista, columns = ["Ano", "Filme", "Nota IMDb"])

	# definindo o database
	conn = sqlite3.connect('../../database/imdb.db')
	df.to_sql('all_imdb', conn)

	return
