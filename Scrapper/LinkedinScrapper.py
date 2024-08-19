from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Links.LinkedinLinks import LinkedinLinks
from Scrapper.GeneralScrapper import General_Scrapper
import time

class Linkedin_Scrapper(General_Scrapper):

	def __init__(self, **kwargs):
		super().__init__()
		self.email = kwargs.get("email", "")
		self.password = kwargs.get("password","")

	def login(self):

		# Open LinkedIn login page
		self.driver.get(LinkedinLinks.get_url(LinkedinLinks.LOGIN))

		# Enter username
		username_input = self.driver.find_element(By.ID, "username")
		username_input.send_keys(self.email)  # Replace with your LinkedIn username

		# Enter password
		password_input = self.driver.find_element(By.ID, "password")
		password_input.send_keys(self.password)  # Replace with your LinkedIn password

		# Submit the login form
		password_input.send_keys(Keys.RETURN)
		
		# Wait for login to finish
		WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "global-nav-search")))

	def __load_all_connections(self):
		# Scroll to the bottom of the page to load all connections
		last_height = self.driver.execute_script("return document.body.scrollHeight")

		while True:
			# Scroll down
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

			# Wait to load the page
			time.sleep(2)

			# Calculate new scroll height and compare with the last scroll height
			new_height = self.driver.execute_script("return document.body.scrollHeight")
			if new_height == last_height:
				try:
					show_more_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'scaffold-finite-scroll__load-button')]")
					ActionChains(self.driver).move_to_element(show_more_button).click().perform()
				except NoSuchElementException:
					print("Button not found and hit the last of the page")
					break
			last_height = new_height

	def get_email_of_connections(self):
		# Navigate to connections page (You may need to adjust this URL based on your LinkedIn layout)
		self.driver.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')
		
		# Wait until the connections list is loaded
		WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.scaffold-finite-scroll__content")))

		# load all connections
		self.__load_all_connections()

		# Collect all connection names
		connections = self.driver.find_elements(By.CSS_SELECTOR, "span.mn-connection-card__name")
		profile_links = [connection.find_element(By.XPATH, "..").get_attribute('href') for connection in connections]

		for profile in profile_links:
			self.driver.execute_script(f"window.open('');")

			# Switch to the new tab
			self.driver.switch_to.window(self.driver.window_handles[-1])

			# Load the profile page
			self.driver.get(f"{profile}overlay/contact-info/")

			# Wait for the page to load
			time.sleep(3)

			try:
				# Locate the <a> tag using XPath based on the 'mailto:' attribute
				email_element = self.driver.find_element(By.XPATH, "//a[starts-with(@href, 'mailto:')]")

				# Get the href attribute of the <a> element
				email_href = email_element.get_attribute("href").replace("mailto:", "")
				# print(f"Current email: {email_href}")

				self.scraped_emails["emails"].append(email_href)

			except NoSuchElementException:
				print("Email not found")
				continue

			# Close the current tab
			self.driver.close()
    
    		# Switch back to the original tab
			self.driver.switch_to.window(self.driver.window_handles[0])
		
		super().populate_json(self.scraped_emails)