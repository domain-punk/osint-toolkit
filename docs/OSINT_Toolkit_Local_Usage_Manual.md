
# 📘 OSINT Toolkit – Local Usage Manual

This guide will walk you through how to use the OSINT Toolkit locally on your machine to conduct in-depth research on a person, including finding emails, contact details, domains, IPs, and potential mobile numbers.

---

## ✅ Prerequisites

Before starting, make sure you have:

1. Docker & Docker Compose installed (https://docs.docker.com/get-docker/)
2. The `osint-toolkit` project folder extracted
3. A `.env` or `osing.env` file set up with your API keys

---

## 🔧 Setting Up Locally (macOS/Linux)

```bash
cd /path/to/osint-toolkit
cp .env.example osing.env  # Or create manually
```

Edit `osing.env` and add:

```env
HIBP_API_KEY=your_key_here
HUNTER_API_KEY=your_key_here
SHODAN_API_KEY=your_key_here
```

Then run:

```bash
docker-compose up --build
```

Open your browser and go to:

```
http://localhost:8501
```

---

## 🎯 How to Run a Deep Person Search

To find the most comprehensive public info on a target (e.g., John Smith):

### 1. Enter Target Info

Fill in the fields:

- **Full Name**: e.g., `John Smith`
- **Domain** (if known): e.g., `smithlaw.com`
- **Email** (if known)
- **Social Link** (optional): LinkedIn/Facebook profile

---

### 2. Recommended Buttons to Click (in order)

✅ Start with:

- `🌐 WHOIS Lookup` — Get domain ownership, org, registrar
- `🌐 Run Network Intelligence` — Fetch DNS + IP + ASN
- `🌍 Geolocate IP` — Find server/host location
- `🔎 Shodan Scan` — Expose public servers, ports, banners
- `📇 Search Contact Pages` — Crawl for public emails & phones
- `📧 theHarvester` — Scrape email intel from search engines
- `🧵 Check Pastebin for Leaks` — Search for exposed emails
- `🔒 HaveIBeenPwned Check` — Look for breaches
- `📢 Hunter.io Email Verifier` — Validate emails
- `🧠 Generate Entity Map` — Link name → domain → email → org

---

## 📤 Exporting Your Investigation

Once done, scroll to the **Export Results** section and click:

- `Export to CSV` – For spreadsheet or data analysis
- `Export to PDF` – For reports, archives or sharing

---

## 🛠 Troubleshooting

- **Blank output?** Make sure the domain resolves and input is correct
- **API errors?** Check your keys in `osing.env`
- **Docker not starting?** Run `docker-compose down` then `up --build`

---

## ✅ Example Workflow

Investigating: `Linda Rolton`, associated with `charly.co.uk`

1. Full Name: `Linda Rolton`
2. Domain: `charly.co.uk`
3. Click:
   - WHOIS
   - DNS/IP Intelligence
   - Shodan
   - Contact Pages
   - Pastebin
   - HIBP
   - Entity Map
4. Export results

---

For advanced use like dark web integrations, geolocation heatmaps, or scheduled scans, refer to the online GitHub README or contact your developer.
