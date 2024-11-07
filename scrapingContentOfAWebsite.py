import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://innovatoor.com'  

# Send a request to fetch the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the webpage content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Extract all headings (e.g., h1, h2) from the page
    headings = soup.find_all(['h1', 'h2', 'h3'])
    
    for heading in headings:
        print(heading.text.strip())
    
    # Example: Extract all paragraph text
    paragraphs = soup.find_all('p')
    
    for paragraph in paragraphs:
        print(paragraph.text.strip())
    
    # You can customize the extraction based on the structure of the webpage
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")












