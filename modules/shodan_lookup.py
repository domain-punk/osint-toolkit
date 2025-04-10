import requests
def shodan_domain_search(domain, key):
    try:
        ip = requests.get(f'https://api.shodan.io/dns/resolve?hostnames={domain}&key={key}').json().get(domain)
        if not ip: return {'error': 'IP resolution failed'}
        return requests.get(f'https://api.shodan.io/shodan/host/{ip}?key={key}').json()
    except Exception as e: return {'error': str(e)}
