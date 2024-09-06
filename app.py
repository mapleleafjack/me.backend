import logging
from flask import Flask
from sqlalchemy import func
from blueprint.project_blueprint import project_blueprint

from db.connection import check_db_connection, get_session
from db.models import Project

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app.register_blueprint(project_blueprint)
        
@app.route('/')
def home():
    return "Hello, Jack! This is your backend service."

@app.route('/me')
def serve_me_json():
    return app.send_static_file('me.json')

@app.route('/health')
def health():
    if check_db_connection():
        return "Hello, Jack! The database connection is successful."
    else:
        return "Hello, Jack! Failed to connect to the database."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
