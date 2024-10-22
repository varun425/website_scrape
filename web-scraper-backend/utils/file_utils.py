# /backend/utils/file_utils.py
import pandas as pd
import pdfkit

# Function to save data to CSV
def save_to_csv(data):
    df = pd.DataFrame(data)
    csv_path = 'scraped_data.csv'
    df.to_csv(csv_path, index=False)
    return csv_path

# Function to save data to PDF
def save_to_pdf(data):
    df = pd.DataFrame(data)
    html_content = df.to_html(index=False)
    pdf_path = 'scraped_data.pdf'
    pdfkit.from_string(html_content, pdf_path)
    return pdf_path
