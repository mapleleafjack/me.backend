from flask import Blueprint, jsonify, request
from db.connection import get_session
from gateway.project_gateway import ProjectGateway
from usecase.project_usecase import ProjectUseCase

# Define a blueprint
project_blueprint = Blueprint('project_blueprint', __name__)

@project_blueprint.route('/projects', methods=['POST'])
def create_project():
    usecase = ProjectUseCase(ProjectGateway(get_session()))
    description = request.json.get('description')
    project = usecase.add_project(description)
    if project is not None:
        return jsonify(project.serialize()), 201
    else:
        return jsonify({"error": "Failed to create project"}    ), 500
    
@project_blueprint.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    usecase = ProjectUseCase(ProjectGateway(get_session()))
    project = usecase.get_project(project_id)
    if project is not None:
        return jsonify(project.serialize()), 200
    else:
        return jsonify({"error": "Project not found"}), 404
    
@project_blueprint.route('/projects', methods=['GET'])
def get_all_projects():
    usecase = ProjectUseCase(ProjectGateway(get_session()))
    projects = usecase.get_all_projects()
    if projects is not None:
        return jsonify([project.serialize() for project in projects]), 200
    else:
        return jsonify({"error": "Failed to retrieve projects"}), 500
    
@project_blueprint.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    usecase = ProjectUseCase(ProjectGateway(get_session()))
    description = request.json.get('description')
    project = usecase.update_project(project_id, description)
    if project is not None:
        return jsonify(project.serialize()), 200
    else:
        return jsonify({"error": "Failed to update project"}), 500
    
@project_blueprint.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    usecase = ProjectUseCase(ProjectGateway(get_session()))
    result = usecase.delete_project(project_id)
    if result:
        return jsonify({"message": "Project deleted"}), 200
    else:
        return jsonify({"error": "Failed to delete project"}), 500