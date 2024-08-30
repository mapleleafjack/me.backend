import logging
from flask import Flask

from db.connection import check_db_connection

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def home():
    return "Hello, Jack!"
    
@app.route('/health')
def health():
    if check_db_connection():
        return "Hello, Jack! The database connection is successful."
    else:
        return "Hello, Jack! Failed to connect to the database."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
