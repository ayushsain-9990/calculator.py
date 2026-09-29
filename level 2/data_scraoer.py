import csv
import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com/"
    print(f"Fetching data from: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        quote_elements = soup.find_all("div", class_="quote")
        
        scraped_data = []
        for q in quote_elements:
            text = q.find("span", class_="text").get_text(strip=True)
            author = q.find("small", class_="author").get_text(strip=True)
            scraped_data.append([text, author])
            
        csv_file = "scraped_quotes.csv"
        with open(csv_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Quote", "Author"])
            writer.writerows(scraped_data)
            
        print(f"✅ Scraped {len(scraped_data)} quotes successfully!")
        print(f"📁 Saved output to: {csv_file}")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Network/HTTP Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

if __name__ == "__main__":
    scrape_quotes()