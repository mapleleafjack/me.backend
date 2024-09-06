from unittest import mock

from flask import Flask
import pytest

from blueprint.project_blueprint import project_blueprint
from gateway.project_gateway import ProjectGateway


@pytest.fixture
def client():
    # Create a Flask app for testing
    app = Flask(__name__)
    app.register_blueprint(project_blueprint)

    with app.test_client() as client:
        yield client


class TestProjectRoutes:
    @mock.patch.object(ProjectGateway, "add_project")
    def test_add_project(self, mock_add_project, client):
        # Mock the return value of the ProjectGateway.add_project method
        mock_add_project.return_value = mock.Mock(serialize=lambda: {"message": "POST project"})

        # Correct endpoint to create a new project
        response = client.post("/projects", json={"description": "New Project"})

        assert response.status_code == 201
        assert response.get_json() == {"message": "POST project"}


    @mock.patch.object(ProjectGateway, "get_project")
    def test_get_project(self, mock_get_project, client):
        # Mock the return value of the ProjectGateway.get_project method
        mock_get_project.return_value = mock.Mock(serialize=lambda: {"message": "GET project"})

        # Correct endpoint to include project_id
        response = client.get("/projects/1")

        assert response.status_code == 200
        assert response.get_json() == {"message": "GET project"}

    @mock.patch.object(ProjectGateway, "get_all_projects")
    def test_get_all_projects(self, mock_get_all_projects, client):
        # Mock the return value of the ProjectGateway.get_all_projects method
        mock_get_all_projects.return_value = [mock.Mock(serialize=lambda: {"message": "GET all projects"})]

        # Correct endpoint to retrieve all projects
        response = client.get("/projects")

        assert response.status_code == 200
        assert response.get_json() == [{"message": "GET all projects"}]#

    @mock.patch.object(ProjectGateway, "update_project")
    def test_update_project(self, mock_update_project, client):
        # Mock the return value of the ProjectGateway.update_project method
        mock_update_project.return_value = mock.Mock(serialize=lambda: {"message": "PUT project"})

        # Correct endpoint to update a project
        response = client.put("/projects/1", json={"description": "Updated Project"})

        assert response.status_code == 200
        assert response.get_json() == {"message": "PUT project"}

    @mock.patch.object(ProjectGateway, "delete_project")
    def test_delete_project(self, mock_delete_project, client):
        # Mock the return value of the ProjectGateway.delete_project method
        mock_delete_project.return_value = True

        # Correct endpoint to delete a project
        response = client.delete("/projects/1")

        assert response.status_code == 200
        assert response.get_json() == {"message": "Project deleted"}