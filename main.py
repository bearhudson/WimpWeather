from bs4 import BeautifulSoup
import requests

response = requests.get("https://mitoc-trips.mit.edu/")
trips_text = response.text

soup = BeautifulSoup(trips_text, 'html.parser')

for trip in soup.find_all('tbody'):
    print(trip.find_all('a'))
