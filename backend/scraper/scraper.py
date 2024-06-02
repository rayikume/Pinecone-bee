from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

def sanitize_filename(url):
    filename = re.sub(r'[^a-zA-Z0-9_\-]', '_', url)
    return filename[:300]

def scrape_page(driver, url):
    print(f"Navigating to {url}")
    driver.get(url)
    time.sleep(10)

    html_text = driver.page_source
    soup = BeautifulSoup(html_text, 'lxml')
    text_content = soup.get_text(separator='\n', strip=True)

    filename = sanitize_filename(url) + '_text.txt'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text_content)

    print(f"Text content has been written to '{filename}'.")

def main():
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        urls = [
            'https://u.ae/en/information-and-services#/',
            'https://u.ae/en/information-and-services/top-government-services',
            'https://u.ae/en/information-and-services/visa-and-emirates-id',
            'https://u.ae/en/information-and-services/jobs',
            'https://u.ae/en/information-and-services/education',
            'https://u.ae/en/information-and-services/business',
            'https://u.ae/en/information-and-services/moving-to-the-uae',
            'https://u.ae/en/information-and-services/justice-safety-and-the-law',
            'https://u.ae/en/information-and-services/visiting-and-exploring-the-uae',
            'https://u.ae/en/information-and-services/transportation',
            'https://u.ae/en/information-and-services/finance-and-investment',
            'https://u.ae/en/information-and-services/environment-and-energy',
            'https://u.ae/en/information-and-services/housing',
            'https://u.ae/en/information-and-services/health-and-fitness',
            'https://u.ae/en/information-and-services/passports-and-traveling',
            'https://u.ae/en/information-and-services/public-holidays-and-religious-affairs',
            'https://u.ae/en/information-and-services/infrastructure',
            'https://u.ae/en/information-and-services/social-affairs',
            'https://u.ae/en/information-and-services/charity-and-humanitarian-work',
            'https://u.ae/en/information-and-services/g2g-services',
        ]

        for url in urls:
            time.sleep(10)
            scrape_page(driver, url)
            time.sleep(10)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()


    