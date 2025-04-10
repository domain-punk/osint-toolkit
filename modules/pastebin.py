import requests
from bs4 import BeautifulSoup
def search_pastebin(keyword):
    try:
        q = f'site:pastebin.com {keyword}'
        r = requests.get(f'https://www.google.com/search?q={q.replace(" ", "+")}', headers={'User-Agent': 'Mozilla'})
        soup = BeautifulSoup(r.text, 'html.parser')
        return list({a['href'] for a in soup.find_all('a', href=True) if 'pastebin.com/' in a['href']})
    except: return ['No results or blocked']
