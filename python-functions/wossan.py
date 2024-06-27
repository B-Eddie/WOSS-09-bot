import requests
from bs4 import BeautifulSoup

def retrieve_announcements():
    url = "https://wosann.hdsb.ca/WOSSannouncements/"  # Replace with the URL of the website you want to scrape
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        announcements = soup.find_all("div", class_="aud")
        for announcement in announcements:
            return(f"**{announcement.find('h2').text}**")
            return(announcement.find('p').text)
    else:
        return("Failed to retrieve announcements.")

retrieve_announcements()
