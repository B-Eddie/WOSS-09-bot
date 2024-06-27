import requests
from bs4 import BeautifulSoup
import discord

def retrieve_announcements():
    url = "https://wosann.hdsb.ca/WOSSannouncements/"  # Replace with the URL of the website you want to scrape
    response = requests.get(url)
    return_text = ""
    title = ""
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        announcements = soup.find_all("div", class_="aud")
        title_soup = soup.find_all("div", class_="title") 
        title_string = str([i.text.strip() for i in title_soup])
        title += f"**{title_string[2:-2]}**" # adds a title to the start of the string
        for announcement in announcements:
            return_text += (f"\n**{announcement.find('h2').text}**\n")
            return_text += (f"{announcement.find('p').text}\n")
    else:
        return("Failed to retrieve announcements.")
    embed = discord.Embed(
        title=title,
        description=return_text,
        color=discord.Color.blue()
    )
    return embed
retrieve_announcements()
