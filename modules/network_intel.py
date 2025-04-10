import socket, requests
def get_dns_info(domain):
    try: return {'Domain': domain, 'Resolved IP': socket.gethostbyname(domain)}
    except: return {'error': 'DNS failed'}
def get_ip_info(ip):
    try:
        r = requests.get(f'https://ipinfo.io/{ip}/json')
        return r.json()
    except: return {'error': 'IP lookup failed'}
