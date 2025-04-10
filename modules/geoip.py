import requests
def ip_geolocation(ip):
    try:
        r = requests.get(f'http://ip-api.com/json/{ip}')
        return r.json()
    except: return {'error': 'GeoIP failed'}
