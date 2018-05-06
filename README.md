# Videoken
Scraping data files (to be used to extract pdf for Videoken)

Languages used : python 3.5.0

Python Libraries used : Selenium,BeautifulSoup,requests,urllib.request,re

Headless browsers used : Mozilla Firefox v55+ (https://developer.mozilla.org/en-US/Firefox/Headless_mode)

External dependencies : Latest Geckodriver needed (https://github.com/mozilla/geckodriver/releases)


1. Open the terminal in a new directory (preferably) to download all the files to

2. Run the python script in Terminal inside that directory using :  python3 scrape.py

3. Type the necessary academic topic or sub-topic like :Machine Learning or :Operating Systems (preferably avoid abbreviations like OS or ML)

4. Scraping begins from the printed URL and download links are extracted 

5. Files are being downloaded or in case file is absent "FILE NOT AVAILABLE" is printed

5. Approximately not more than 7-8 minutes depending on the network connectivity will be needed to start downloading files
