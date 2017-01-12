import pandas
import requests
from bs4 import BeautifulSoup

base_url = 'http://www.theagapecenter.com/Hospitals/'
loc = 'Washington'
url = base_url+loc
agape_url = requests.get(url)
agape_soup = BeautifulSoup(agape_url.text, 'html.parser')
letters = agape_soup.find_all('tr')


def t():
	i = 6
	l = []
	s = set()
	d = {}
	while i < 250:
		try:
			#if letters[i].has_attr('a'):
			#print(i)
			l.append(' '.join(letters[i].a.get_text().split()))
			s.add(' '.join(letters[i].a.get_text().split()))
			d[' '.join(letters[i].a.get_text().split())] = letters[i].a['href']
		except IndexError as ie:
			print(ie)
		i += 1
	return l,s, d

