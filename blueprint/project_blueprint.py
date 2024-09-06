
from flask import app

from db.connection import get_session
from gateway.project_gateway import ProjectGateway
from usecase.project_usecase import ProjectUseCase


@app.route('/projects', methods=['POST'])
def create_project():
    usecase = ProjectUseCase(ProjectGateway(get_session()))  

@app.route('/projects', methods=['GET'])
def list_projects():
    

@app.route('/projects', methods=['DELETE'])
def delete_projects():
