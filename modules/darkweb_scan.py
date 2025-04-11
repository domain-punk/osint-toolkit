
import requests
from bs4 import BeautifulSoup

def search_ahmia(keyword):
    try:
        query = keyword.replace(' ', '+')
        url = f"https://ahmia.fi/search/?q={query}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        results = []
        for res in soup.find_all('div', class_='result'):
            title_tag = res.find('a')
            snippet = res.find('p')
            if title_tag and title_tag.get('href'):
                results.append({
                    'title': title_tag.text.strip(),
                    'link': title_tag['href'],
                    'snippet': snippet.text.strip() if snippet else ''
                })
        return results
    except Exception as e:
        return [{"error": str(e)}]

def search_onionland(keyword):
    try:
        query = keyword.replace(' ', '+')
        url = f"https://onionlandsearchengine.com/search?q={query}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        results = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            if ".onion" in href:
                results.append({
                    'title': a.text.strip(),
                    'link': href,
                    'snippet': ''
                })
        return results
    except Exception as e:
        return [{"error": str(e)}]

def search_darksearch(keyword, api_key):
    try:
        url = f"https://darksearch.io/api/search?query={keyword}"
        headers = {"Authorization": api_key, "Accept": "application/json"}
        r = requests.get(url, headers=headers, timeout=15)
        data = r.json()
        results = []
        for item in data.get("data", []):
            results.append({
                "title": item.get("title", "No title"),
                "link": item.get("link"),
                "snippet": item.get("snippet", "")
            })
        return results
    except Exception as e:
        return [{"error": str(e)}]
