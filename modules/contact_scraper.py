import re, requests
from bs4 import BeautifulSoup
def scrape_contact_info(domain):
    urls = [f'http://{domain}/{p}' for p in ['contact', 'about', 'team']]
    results = {'emails': [], 'phones': []}
    for url in urls:
        try:
            soup = BeautifulSoup(requests.get(url, timeout=5).text, 'html.parser')
            text = soup.get_text()
            results['emails'] += re.findall(r'[\w\.-]+@[\w\.-]+', text)
            results['phones'] += re.findall(r'\+?\d[\d\s().-]{7,}\d', text)
        except: continue
    return results
