from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape')
def scrape_data():
    url = "https://www.justdial.com/Delhi/Web-Designing-Services/nct-10589480"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    companies = []
    for item in soup.select(".cntanr"):
        name = item.select_one(".lng_cont_name")
        phone = item.select_one(".contact-info")
        address = item.select_one(".cont_sw_addr")

        if name:
            companies.append({
                "Name": name.get_text(strip=True),
                "Phone": phone.get_text(strip=True) if phone else "N/A",
                "Address": address.get_text(strip=True) if address else "N/A"
            })

    return jsonify(companies)
