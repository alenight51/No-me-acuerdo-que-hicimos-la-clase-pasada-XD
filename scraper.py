from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv 

start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Edge("C:\Users\Aleja\OneDrive\Documents\Coding\edgedriver_win64\msedgedrive.exe")
browser.get(start_url)
time.sleep(10)
def scraper():
    headers = ["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]
    planet_data = []
    for i in range(0, 221):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags = ul_tag.find_all("li")