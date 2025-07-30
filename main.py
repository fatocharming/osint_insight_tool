import requests
from bs4 import BeautifulSoup
import json

def get_ip_info(ip_address):
    """Fetches IP information from an external API."""
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    return response.json()

def scrape_website(url):
    """Scrapes the website title and meta description."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string if soup.title else 'No title found'
    meta_description = soup.find('meta', attrs={'name': 'description'})
    description = meta_description['content'] if meta_description else 'No description found'
    return title, description

def main():
    """Main function for OSINT tasks."""
    # Example IP address
    ip_address = '8.8.8.8'
    ip_info = get_ip_info(ip_address)
    print("IP Information:", json.dumps(ip_info, indent=2))
    
    # Example website
    url = 'https://www.example.com'
    title, description = scrape_website(url)
    print("Website Title:", title)
    print("Meta Description:", description)

if __name__ == "__main__":
    main()