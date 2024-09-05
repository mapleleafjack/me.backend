import logging
from flask import Flask, g, jsonify, request

from db.connection import check_db_connection, get_session
from service.project_service import add_project, get_projects
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a session for each request
@app.before_request
def before_request():
    g.session = get_session()

@app.teardown_request
def teardown_request(exception):
    session = getattr(g, 'session', None)
    if session is not None:
        session.close()
        
@app.route('/')
def home():
    return "Hello, Jack!"
    
@app.route('/health')
def health():
    if check_db_connection():
        return "Hello, Jack! The database connection is successful."
    else:
        return "Hello, Jack! Failed to connect to the database."

@app.route('/projects', methods=['POST'])
def create_project():
    """Create a new project."""
    data = request.json
    description = data.get('description')
    if not description:
        return jsonify({'error': 'Description is required'}), 400
    
    try:
        project = add_project(description, g.session)
        return jsonify({'id': project.id, 'description': project.description}), 201
    except SQLAlchemyError as e:
        logging.error(f"Error creating project: {e}")
        return jsonify({'error': 'Failed to create project'}), 500

@app.route('/projects', methods=['GET'])
def list_projects():
    """List all projects."""
    try:
        projects = get_projects(g.session)
        return jsonify([{'id': project.id, 'description': project.description} for project in projects]), 200
    except SQLAlchemyError as e:
        logging.error(f"Error retrieving projects: {e}")
        return jsonify({'error': 'Failed to retrieve projects'}), 500

@app.route('/projects', methods=['DELETE'])
def delete_projects():
    """Delete all projects."""
    try:
        delete_projects(g.session)
        return jsonify({'message': 'All projects have been deleted'}), 200
    except SQLAlchemyError as e:
        logging.error(f"Error deleting projects: {e}")
        return jsonify({'error': 'Failed to delete projects'}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
