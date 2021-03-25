import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys

class Fetcher:
	def __init__(self, url):
		self.options = webdriver.ChromeOptions()
		self.options.add_argument('--ignore-certificate-errors')
		self.options.add_argument('--incognito')
		self.options.add_argument('--headless')
		self.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=self.options)
		self.url = url
		

	def lookup(self):
		self.driver.get(self.url)
		div = self.driver.find_elements_by_class_name("xpdopen")
		soup = BeautifulSoup(self.driver.page_source, "lxml")
		text = soup.find('div', class_='Z0LcW XcVN5d')
		if text == None:
			text = soup.find('div', class_='Z0LcW XcVN5d AZCkJd')
			if text == None:
				ans = "No luck, let my open the browser for more"
			else:
				ans = text.get_text()	
		else:
				ans = text.get_text()
		   
		self.driver.quit()
		return ans	
					