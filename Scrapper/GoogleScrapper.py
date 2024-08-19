from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Scrapper.GeneralScrapper import General_Scrapper
from Links.GoogleLinks import GoogleLinks
import time

class Google_Scrapper(General_Scrapper):

	def __init__(self, **kwargs):
		super().__init__()
		self.position = kwargs["position"]
		self.location = kwargs["location"]
		self.domain = kwargs["domain"]

	def search_with_query(self):
		url = GoogleLinks.get_url({ "position": self.position, "location": self.location, "domain": self.domain })
		# print(url)
		self.driver.get(url)
