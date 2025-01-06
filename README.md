# Twitter Trends Scraper

## Project Description
The Twitter Trends Scraper is a Python-based project that uses Selenium and Flask to scrape trending topics from Twitter. The project integrates ProxyMesh for proxy usage and MongoDB for storing the scraped data. A Flask web application provides a simple interface to run the scraper and display the trending topics along with metadata like the IP address used for the query.

## Tech Stack
- **Programming Languages:** Python
- **Frameworks:** Flask
- **Web Scraping Library:** Selenium
- **Database:** MongoDB
- **Proxy Service:** ProxyMesh
- **Frontend:** HTML (via Flask templates)

## How to Setup the Project

### 1. Clone the Repository
```bash
https://github.com/YashK13200/twitter-trends-scraper.git
cd twitter-trends-scraper
```

### 2. Install Required Dependencies
Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

### 3. Set Up Configuration
Edit the `config.json` file and fill in the required details:
```json
{
    "proxymesh_url": "http://USERNAME:PASSWORD@proxymesh.com:31280",
    "chromedriver_path": "<path_to_chromedriver>",
    "twitter_username": "<your_twitter_username>",
    "twitter_password": "<your_twitter_password>",
    "mongo_uri": "mongodb+srv://<username>:<password>@cluster.mongodb.net/test"
}
```
- **`proxymesh_url`**: Replace `USERNAME` and `PASSWORD` with your ProxyMesh account credentials.
- **`chromedriver_path`**: Specify the absolute path to the ChromeDriver executable installed on your system.
- **`twitter_username`**: Enter your Twitter account username.
- **`twitter_password`**: Enter your Twitter account password.
- **`mongo_uri`**: Provide the connection URI for your MongoDB database.

### 4. Run the Flask Application
Start the Flask server:
```bash
python app.py
```

### 5. Access the Web Page
Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

### 6. Scrape Twitter Trends
Click the button on the webpage to scrape the latest trending topics from Twitter. The data will be displayed on the page and stored in your MongoDB database.

## Features
- Login to Twitter using Selenium.
- Scrape trending topics from Twitter.
- Store the scraped data in MongoDB.
- Display the data on a Flask-powered webpage.
- Use ProxyMesh for proxy handling.

## Notes
- Ensure you have ChromeDriver installed and that it matches the version of Chrome installed on your machine.
- Make sure to use valid ProxyMesh credentials and MongoDB connection details.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.
