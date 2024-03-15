import requests
from bs4 import BeautifulSoup
import json

# Base URL of the website without a trailing slash
BASE_URL = "https://festivalfans.nl"


def scrape_festival_details(event_relative_url):
    """
    Scrapes detailed information from a festival's detail page.
    :param event_relative_url: The relative URL to the festival detail page.
    :return: A dictionary containing detailed information about the festival.
    """
    # Correctly construct the full URL for the detail page
    detail_url = BASE_URL + event_relative_url

    # Make a request to the detail page
    response = requests.get(detail_url)
    soup = BeautifulSoup(response.content, "html5lib")

    # Initialize a dictionary to store the details
    details = {}

    # Find the information table
    info_table = soup.find("table", attrs={"class": "info-table"})
    if info_table:
        for row in info_table.find_all("tr"):
            # Extract each row of the table
            columns = row.find_all("td")
            if len(columns) == 2:
                # The first column will be the key, and the second column will be the value
                key = columns[0].text.strip().lower().replace(" ", "_")
                value = columns[1].text.strip()
                details[key] = value

    return details


# Function to scrape the main page and get festival details
def scrape_main_page():
    URL = BASE_URL + "/agenda/"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "html5lib")

    festivals = []

    all_festivals = soup.find_all("div", attrs={"class": "festival-informatie"})

    for festival in all_festivals:
        # Extract the relative URL for the detail page of the festival
        detail_link = festival.find("a", href=True)
        if detail_link:
            event_relative_url = detail_link['href']
            # Make sure it's a relative URL, not an absolute one
            if event_relative_url.startswith(BASE_URL):
                event_relative_url = event_relative_url[len(BASE_URL):]
            # Scrape the detailed information from the detail page
            festival_details = scrape_festival_details(event_relative_url)
            festivals.append(festival_details)
            print(festival_details)

    # Dump the collected festival details into a JSON file
    filename = 'detailed_festivals_data.json'
    with open(filename, 'w') as f:
        json.dump(festivals, f, indent=4)


# Call the function to start the scraping process
scrape_main_page()
