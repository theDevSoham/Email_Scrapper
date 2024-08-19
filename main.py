from Scrapper.Scrapper import Scrapper
import json
import time

if __name__ == "__main__":
	with open("config.json") as config_file:
		data = json.load(config_file)

	scrapper = Scrapper(**data)
	scrapper.initiate_scraping()

	while(True):
		try:
			time.sleep(1)
		except KeyboardInterrupt:
			print("\n\nEnded script lifecycle")
			break
		except Exception as e:
			print(f"\n\nError: Script ended with exception {e}")
			break