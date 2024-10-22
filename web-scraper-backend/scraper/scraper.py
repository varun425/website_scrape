from bs4 import BeautifulSoup
import requests

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all text from the website
    data = {'tag': [], 'text': []}
    
    # Iterate over all elements in the HTML
    for tag in soup.find_all(True):  # 'True' finds all tags
        # Get the tag name
        data['tag'].append(tag.name)
        # Get the text content of the tag, stripping extra whitespace
        text = tag.get_text(strip=True)
        # Check if the text is not empty before appending
        if text:
            data['text'].append(text)

    return data
