import React, { useState } from 'react';
import axios from 'axios';
import './App.css';  // Import the CSS file

function App() {
  const [url, setUrl] = useState('');
  const [scrapedData, setScrapedData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleScrape = async () => {
    if (!url) {
      setError('Please enter a valid URL.');
      return;
    }

    setLoading(true);
    setError('');
    setScrapedData(null);

    try {
      const response = await axios.post('http://127.0.0.1:5000/scrape', { url });
      setScrapedData(response.data);
    } catch (err) {
      setError('Failed to scrape the website. Please check the URL.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="container">
        <h1 className="title">Website Scraper</h1>
        <div className="input-container">
          <input 
            type="text" 
            placeholder="Enter website URL" 
            value={url} 
            onChange={(e) => setUrl(e.target.value)} 
            className="url-input"
          />
          <button onClick={handleScrape} disabled={loading} className="scrape-btn">
            {loading ? 'Scraping...' : 'Scrape Website'}
          </button>
        </div>

        {error && <p className="error-msg">{error}</p>}
        
        {scrapedData && (
          <div className="result-container">
            <p className="success-msg">{scrapedData.message}</p>
            <div className="download-links">
              <a href={`http://127.0.0.1:5000${scrapedData.csv_url}`} download="scraped_data.csv" className="download-btn">Download CSV</a>
              <a href={`http://127.0.0.1:5000${scrapedData.pdf_url}`} download="scraped_data.pdf" className="download-btn">Download PDF</a>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
