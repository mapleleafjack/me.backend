import logging
from flask import Flask, g, jsonify, request

from blueprint import project_blueprint
from db.connection import check_db_connection, get_session
from usecase.project_usecase import add_project, get_projects
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app.register_blueprint(project_blueprint)
        
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
