# /backend/app.py
from flask import Flask, request, jsonify, send_file
from scraper.scraper import scrape_website
from utils.file_utils import save_to_csv, save_to_pdf
import os
from flask_cors import CORS  # Import the CORS library

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Route to scrape website and return links for CSV and PDF downloads
@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json.get('url')

    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        # Scrape website content
        data = scrape_website(url)

        # Save data as CSV and PDF
        csv_path = save_to_csv(data)
        pdf_path = save_to_pdf(data)

        return jsonify({
            'message': 'Scraping successful',
            'csv_url': f'/download/csv',
            'pdf_url': f'/download/pdf'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to download CSV file
@app.route('/download/csv', methods=['GET'])
def download_csv():
    csv_path = 'scraped_data.csv'
    return send_file(csv_path, as_attachment=True)

# Route to download PDF file
@app.route('/download/pdf', methods=['GET'])
def download_pdf():
    pdf_path = 'scraped_data.pdf'
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
