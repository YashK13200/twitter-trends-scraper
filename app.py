from flask import Flask, render_template
from scraper import scrape_trending_topics

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run-script")
def run_script():
    result = scrape_trending_topics()
    return render_template(
        "index.html",
        date_time=result['end_time'],
        trends=[result['trend1'], result['trend2'], result['trend3'], result['trend4'], result['trend5']],
        ip_address=result['ip_address']
    )

if __name__ == "__main__":
    app.run(debug=True)