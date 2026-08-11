import os
import re
import requests
from bs4 import BeautifulSoup

TARGET_URLS = {
    "CS_Advisor": "https://ics.uci.edu/academics/undergrad/contact/",
    "Enrollment_Policies": "https://www.ics.uci.edu/ugrad/policies/",
    "Major_Requirements": "https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/departmentofcomputerscience/computerscience_bs/#requirementstext"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def clean_html_content(soup):
    for element in soup(["script", "style", "nav", "footer", "header", "aside"]):
        element.decompose()
        
    main_content = soup.find("div", id="content") or soup.find("main") or soup.body
    text = main_content.get_text(separator="\n")
    cleaned_text = re.sub(r"\n\s*\n", "\n\n", text)
    return cleaned_text.strip()

def run_scraper():
    os.makedirs("data", exist_ok=True)
    print("Starting Automated Web Scraping Pipeline for UCI ICS...")
    for filename, url in TARGET_URLS.items():
        try:
            print(f" Fetching: {url}")
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
            clean_text = clean_html_content(soup)

            output_path = f"data/{filename}.md"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(f"# Official Scraped Data: {filename}\n")
                f.write(f"**Source URL:** {url}\n\n")
                f.write("=" * 80 + "\n\n")
                f.write(clean_text)

            print(f" Successfully saved cleaned data to {output_path}")

        except Exception as e:
            print(f" Error scraping {url}: {e}")

if __name__ == "__main__":
    run_scraper()
