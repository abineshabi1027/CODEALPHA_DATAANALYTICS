import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_quotes(url):
    """
    Fetches quotes, authors, and tags from the provided URL.
    """
    print(f"Fetching data from: {url}")
    
    # 1. Send an HTTP GET request to the location
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []

    # 2. Parse the HTML structure using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 3. Identify and collect relevant data
    # The website wraps each quote in a <div class="quote">
    quotes_data = []
    quote_elements = soup.find_all('div', class_='quote')
    
    for element in quote_elements:
        # Extract the text of the quote
        text = element.find('span', class_='text').get_text(strip=True)
        
        # Extract the author's name
        author = element.find('small', class_='author').get_text(strip=True)
        
        # Extract the tags associated with the quote
        tags_elements = element.find_all('a', class_='tag')
        tags = [tag.get_text(strip=True) for tag in tags_elements]
        # Join tags into a single comma-separated string for easier analysis later
        tags_string = ", ".join(tags)
        
        # Append a dictionary to our list
        quotes_data.append({
            'Quote': text,
            'Author': author,
            'Tags': tags_string
        })
        
    return quotes_data

def create_dataset(data, filename="scraped_quotes_dataset.csv"):
    """
    Converts the scraped data into a custom dataset (CSV format).
    """
    if not data:
        print("No data to save.")
        return
        
    # Create a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False, encoding='utf-8')
    print(f"Successfully saved {len(data)} records to '{filename}'.")

# --- Main Execution ---
if __name__ == "__main__":
    # The 'correct location' for this practice project
    target_url = "http://quotes.toscrape.com/"
    
    # Run the scraper
    scraped_data = scrape_quotes(target_url)
    
    # Create the custom dataset
    create_dataset(scraped_data)
