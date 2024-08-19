from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import json

class General_Scrapper:

	def __init__(self):
		self.scraped_emails = {"emails": []}
		self.driver = self.__setup_driver()

	def __setup_driver(self):
		# Configure options for ChromeDriver
		options = Options()
		options.add_argument("--start-maximized")  # Start browser maximized
		options.add_argument("--disable-infobars")
		options.add_argument("--disable-extensions")

		# Initialize the ChromeDriver
		service = Service(ChromeDriverManager().install())
		driver = webdriver.Chrome(service=service, options=options)
		return driver
	
	def __read_json(self, file_path):
		"""Read JSON data from a file, return an empty dictionary if the file doesn't exist."""
		if os.path.exists(file_path):
			with open(file_path, 'r') as file:
				return json.load(file)
		return {}
	
	def __write_json(self, file_path, data):
		"""Write JSON data to a file."""
		with open(file_path, 'w') as file:
			json.dump(data, file, indent=4)
	
	def populate_json(self, new_data):

		# Define the project root directory
		project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Directory where the script is located

		# Define the directory and file path
		directory = os.path.join(project_root, 'Outputs')
		file_path = os.path.join(directory, 'outputs.json')

		# Ensure the directory exists
		os.makedirs(directory, exist_ok=True)

		# Read existing data from the file
		existing_data = self.__read_json(file_path)

		# Update the existing data with new data
		existing_data.update(new_data)

		# Write the updated data back to the file
		self.__write_json(file_path, existing_data)

		print(f"Data successfully written to {file_path}")
