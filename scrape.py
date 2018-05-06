from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request, urlretrieve
from urllib.parse import quote
import re
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import requests
import urllib.request

############################################################
def file_download(url):
	print("Downloading from " + url)
	file_name = url.split('/')[-1]
	
	try :	
		r = requests.get(url, stream=True)
		if r.status_code == 200:
			with open(file_name, 'wb') as fd:
				for chunk in r.iter_content(chunk_size = 10000000):
					fd.write(chunk)
				print("Downloaded file-name is " + file_name)
	except :
		urllib.request.urlretrieve(url,file_name)
		print("Downloaded file-name is " + file_name)

###############################################################
raw = input("Please enter the topic for scraping files (like Machine Learning,Data science ...):")
string = quote(raw)
#query = (raw)
print("Query topic given :" + " " + raw + " ")
url = "https://www.pdfdrive.net/"

url_search= "https://www.pdfdrive.net/search?q="
url_page = "&page="
url_new = url_search + string + url_page


new_list = []

#SELECTED 20 PAGES(MAXIMUM NUMBER) AS PER DESIGN OF pdfdrive.net HTML
for pagenum in range(20):
	url_new = url_search + string + url_page + str(pagenum + 1)	
	print(url_new)
	req = urllib.request.Request(url_new,headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
	hh = urllib.request.urlopen(req)
	try:	
		bsObj = BeautifulSoup(hh)
		links_list=[]
	#bsObj.findAll('a', attrs={'href': re.compile("html")})

		for link in bsObj.findAll('a', attrs={'href': re.compile("html")}):
			links_list.append(url + link.get('href') ) 
		links_list = list(set(links_list))	
		for element in links_list:	
			new_list.append( element )
	except:
		pass
#debugging
#print(new_list)
#print(len(new_list))

#TAKES 2 MINUTES IF ALL 20 SEARCH PAGES(DEFAULT) ARE SCRAPED

d_list=[]
for row in range(len(new_list)) : 
	try:	
		print("Links to be scrap from " + new_list[row])  		
		uu = urlopen(new_list[row])
		Obj = BeautifulSoup(uu) 
		new = Obj.findAll("a",{"rel" : "nofollow"})
		d_link = new[0]['href']
		d_list.append(url + d_link) 
	except:
		pass		


pdf_link=[]

#TAKES 6 MINUTES IF ALL 20 SEARCH PAGES(DEFAULT) ARE SCRAPED

for row in range(len(d_list)) :
	
	print("Trying for Link: " + d_list[row])
	options = Options()
	options.add_argument('-headless')
	driver = Firefox(executable_path='/usr/local/bin/geckodriver', firefox_options=options)
	driver.get(d_list[row])

	try:
		
		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "file-available")))

		#for debugging purposes		
		#print(element)
		#print(driver.find_element_by_id("content").text)

		element2 = driver.find_element_by_id("file-available")
		html = element2.get_attribute('outerHTML')
		val = BeautifulSoup(html,'html.parser').a.attrs['href']

		file_download(val)	
		pdf_link.append(val) 
		driver.close()	
		
	except:
		print("FILE NOT AVAILABLE")
		pass


#For retriving all the pdf_Links together as a list use pdf_link
#print(pdf_link)

