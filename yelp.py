base_url = 'https://www.yelp.com/search?find_desc='
provider = givenProvider
location = givenLocation
'&find_loc=Seattle%2C+WA%2C+US&ns=1'

def lookup(givenProvider, givenLocation):
	provider = givenProvider
	location = givenLocation
	pageNumber = 0
	while pageNumber < 200:
		#print('Before', url)
		url = base_url + provider + "&find_loc=" + location + "&start=" + str(pageNumber)
		print('After', url)
		yelp_url = requests.get(url)
		yelp_bs = BeautifulSoup(yelp_url.text, 'html.parser')
        #agape_soup = BeautifulSoup(agape_url)
        #print(agape_soup.prettify())
		provider = yelp_bs.find_all('div', {'class': 'biz-listing-large'})
		for elem in provider:
			providerName = elem.findAll('a', {'class':'biz-name'})[0].text
			print(providerName)
			try:
				providerAddress = elem.findAll('address')[0].contents
				if not providerAddress:
					raise ValueError('No Address available')
					providerAddress = 'NONE'
				for line in providerAddress:
					if 'br' in str(line):
						print(line.getText().strip(' \n\t\r'))
					else:
						print(line.strip(' \n\t\r'))
				#print(providerAddress)
				providerPhone = elem.findAll('span', {'class':'biz-phone'})[0].text
				if not providerPhone:
					raise ValueError('No phone available')
					providerPhone = 'NONE'
			except ValueError as ve:
				print(ve)


			print(providerPhone)

		pageNumber += 10


    dic = {}
    for elem in letters:
			try:
				dic[elem.a.get_text()] = {}
			except Exception as e:
				print(type(e))



        #print(letters[50].a['href'].text)
        #lobb = {}
        #for i in letters:
            #lobb[i.a.get_text()] = {}
        #hosp = agape_soup.findAll('a', {'class' :'citytown'})
        #hosp = agape_soup.findAll('a', href=re.compile('http'))
        #n = 0

