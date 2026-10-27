
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Cloud Computing Lab</h1>
    <h2>Azure App Service - PaaS</h2>
    <p>My web application is running successfully on Microsoft Azure.</p>
    """

if __name__ == "__main__":
    app.run()
