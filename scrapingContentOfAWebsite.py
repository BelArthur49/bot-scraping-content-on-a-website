import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://innovatoor.com'  # Replace with the actual URL if needed

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











from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Define the URL you want to scrape
url = 'https://www.isuzume.rw/'
driver.get(url)

# Set up WebDriverWait with a 30-second timeout
wait = WebDriverWait(driver, 30)

try:
    # Print page source for debugging (optional)
    print(driver.page_source)  # Use this to check if the page content is loaded correctly

    # Example: Wait for and print all headings (h1, h2, etc.)
    try:
        headings = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h1, h2, h3'))
        )
        for heading in headings:
            print(heading.text)
    except TimeoutException:
        print("Timed out waiting for headings.")

    # Example: Wait for and print all paragraph texts
    try:
        paragraphs = wait.until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'p'))
        )
        for paragraph in paragraphs:
            print(paragraph.text)
    except TimeoutException:
        print("Timed out waiting for paragraphs.")

    # Example: Wait for and print all links
    try:
        links = wait.until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'a'))
        )
        for link in links:
            href = link.get_attribute('href')
            if href:  # Print only if href is not empty
                print(href)
    except TimeoutException:
        print("Timed out waiting for links.")

finally:
    # Close the WebDriver
    driver.quit()
