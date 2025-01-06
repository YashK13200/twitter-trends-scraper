import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient
import uuid
import json
from datetime import datetime

# Load ProxyMesh configuration
with open('config.json') as config_file:
    config = json.load(config_file)

# MongoDB setup
client = MongoClient(config['mongo_uri'])
db = client['trending_topics']
collection = db['twitter_trends']

def scrape_trending_topics():
    # Selenium options
    chrome_options = Options()
    chrome_options.add_argument(f"--proxy-server={config['proxymesh_url']}")

    # Set up the WebDriver
    service = Service(config['chromedriver_path'])
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://twitter.com/login")
        time.sleep(5)  # Wait for page load

        # Log in to Twitter
        username = driver.find_element(By.NAME, "text")
        username.send_keys(config['twitter_username'])
        username.send_keys(Keys.RETURN)
        time.sleep(3)

        password = driver.find_element(By.NAME, "password")
        password.send_keys(config['twitter_password'])
        password.send_keys(Keys.RETURN)
        time.sleep(5)

        # Scrape trending topics
        trends = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='trend']")
        trending_topics = [trend.text for trend in trends[:5]]

        # Capture metadata
        ip_address = driver.execute_script("return document.querySelector('body').innerHTML.match(/\d+\.\d+\.\d+\.\d+/)[0];")
        unique_id = str(uuid.uuid4())
        end_time = datetime.now()

        # Store in MongoDB
        record = {
            "_id": unique_id,
            "trend1": trending_topics[0] if len(trending_topics) > 0 else None,
            "trend2": trending_topics[1] if len(trending_topics) > 1 else None,
            "trend3": trending_topics[2] if len(trending_topics) > 2 else None,
            "trend4": trending_topics[3] if len(trending_topics) > 3 else None,
            "trend5": trending_topics[4] if len(trending_topics) > 4 else None,
            "end_time": end_time,
            "ip_address": ip_address
        }
        collection.insert_one(record)

        return record

    finally:
        driver.quit()