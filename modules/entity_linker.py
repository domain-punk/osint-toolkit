def generate_entity_map(name, email, domain, data):
    links = []
    if name: links.append(f'Person: {name}')
    if email: links.append(f'{name or "?"} ↔ Email: {email}')
    if domain: links.append(f'{name or "?"} ↔ Domain: {domain}')
    whois = data.get('WHOIS', {})
    if whois.get('Org'): links.append(f'Domain: {domain} ↔ Org: {whois["Org"]}')
    if whois.get('Registrar'): links.append(f'Domain: {domain} ↔ Registrar: {whois["Registrar"]}')
    return links
