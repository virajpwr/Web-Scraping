import wikipedia
import urllib2
from bs4 import BeautifulSoup
import pandas as pd 

wiki = ["https://en.wikipedia.org/wiki/Pyrus_calleryana", "https://en.wikipedia.org/wiki/Acer_saccharinum", "https://en.wikipedia.org/wiki/Platanus_%C3%97_acerifolia", "https://en.wikipedia.org/wiki/Honey_locust", 
       "https://en.wikipedia.org/wiki/Tilia_tomentosa", "https://en.wikipedia.org/wiki/Quercus_palustris", "https://en.wikipedia.org/wiki/Tilia_americana", "https://en.wikipedia.org/wiki/Tilia_cordata", "https://en.wikipedia.org/wiki/Ulmus_americana", "https://en.wikipedia.org/wiki/Acer_rubrum"]
names = ['callery pear', 'silver maple', 'London planetree','honeylocust','silver linden',
        'pin oak','American Linden', 'littleleaf linden','American elm','red maple']


def scrape(species, name):
	page = urllib2.urlopen(species)
	soup = BeautifulSoup(page)
	all_tables = soup.find_all('table')
	#right_table = soup.find('table', class_ ='infobox biota')
	right_table = soup.find('table',{"class": "infobox biota"})
	print(right_table)
	A = []
	B = []
	#C = []
	#D = [] 
	#E = []
	#F = []
	#G = []
	for row in right_table("tr"):
		cells =  row.findAll('td')
		if len(cells) == 2:
			A.append(cells[0].find(text=True))
			B.append(cells[1].find(text=True))
	df = pd.DataFrame(A, columns=['Title'])
	df[name] = B	
	df.to_csv('red_maple.csv', index = False, encoding='utf-8')
	return df	


#scrape(wiki[0], names[0])
#scrape(wiki[1], names[1])
#scrape(wiki[2], names[2])
#scrape(wiki[3], names[3])
scrape(wiki[9], names[9])