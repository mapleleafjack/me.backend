import pytest
from unittest.mock import MagicMock
from db.models import Project
from gateway.project_gateway import ProjectGateway  # Ensure this is the correct import for your Project model

@pytest.fixture
def mock_session():
    return MagicMock()

@pytest.fixture
def project_gateway(mock_session):
    return ProjectGateway(db_session=mock_session)

def test_get_project(project_gateway, mock_session):
    """Test the get_project method."""
    mock_project = Project(id=1, description="Test Project")
    mock_session.query().filter().one_or_none.return_value = mock_project

    result = project_gateway.get_project(1)

    assert result == mock_project
    mock_session.query().filter().one_or_none.assert_called_once()

def test_get_all_projects(project_gateway, mock_session):
    """Test the get_all_projects method."""
    mock_project = Project(id=1, description="Test Project")
    mock_session.query().all.return_value = [mock_project]

    result = project_gateway.get_all_projects()

    assert result == [mock_project]
    mock_session.query().all.assert_called_once()

def test_add_project(project_gateway, mock_session):
    """Test the add_project method."""

    mock_project = Project(description="New Project")
    mock_session.add.return_value = None 
    mock_session.commit.return_value = None 

    result = project_gateway.add_project("New Project")

    assert result.description == mock_project.description
    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()

def test_update_project(project_gateway, mock_session):
    """Test the update_project method."""
    mock_project = Project(id=1, description="Old Description")
    mock_session.query().filter().one_or_none.return_value = mock_project

    result = project_gateway.update_project(1, "Updated Description")

    assert result.description == "Updated Description"
    mock_session.commit.assert_called_once()

def test_delete_project(project_gateway, mock_session):
    """Test the delete_project method."""
    mock_project = Project(id=1, description="Test Project")
    mock_session.query().filter().one_or_none.return_value = mock_project

    result = project_gateway.delete_project(1)

    assert result is True
    mock_session.delete.assert_called_once()
    mock_session.commit.assert_called_once()
