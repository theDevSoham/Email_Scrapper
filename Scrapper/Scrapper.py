from Scrapper.LinkedinScrapper import Linkedin_Scrapper
from Scrapper.GoogleScrapper import Google_Scrapper
import time

class Scrapper():
	def __init__(self, **kwargs):
		self.engine = kwargs["engine"]
		if kwargs["email"] and kwargs["password"]:
			self.linkedin_email = kwargs["email"]
			self.password = kwargs["password"]
		if kwargs["position"] and kwargs["location"] and kwargs["domain"]:
			self.position = kwargs["position"]
			self.location = kwargs["location"]
			self.domain = kwargs["domain"]

	def initiate_scraping(self):
		# linkedin
		if (self.engine == 'linkedin'):
			print (f"Starting email scrapping for {self.engine}")
			# flow of app
			bot = Linkedin_Scrapper(email = self.linkedin_email, password = self.password)
			bot.login()
			bot.get_email_of_connections()

			time.sleep(2)
			print(f"All emails populated")

		# google
		elif (self.engine == "google"):
			# flow of app
			bot = Google_Scrapper(position = self.position, location = self.location, domain = self.domain)
			bot.search_with_query()