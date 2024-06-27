import requests
from bs4 import BeautifulSoup

def retrieve_announcements():
    url = "https://wosann.hdsb.ca/WOSSannouncements/"  # Replace with the URL of the website you want to scrape
    response = requests.get(url)
    return_text = ""
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        announcements = soup.find_all("div", class_="aud")
        for announcement in announcements:
            return_text += (f"\n**{announcement.find('h2').text}**\n")
            return_text += (f"{announcement.find('p').text}\n")
    else:
        return("Failed to retrieve announcements.")
    return return_text
retrieve_announcements()
