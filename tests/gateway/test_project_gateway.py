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

    mock_project = Project(title="Test Title", description="New Project")
    mock_session.add.return_value = None 
    mock_session.commit.return_value = None 

    # Update the call to include 'title' and 'body'
    result = project_gateway.add_project(title="Test Title", description="New Project", body={'key': 'value'})

    assert result.title == mock_project.title
    assert result.description == mock_project.description
    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()


def test_update_project(project_gateway, mock_session):
    """Test the update_project method."""
    mock_project = Project(id=1, title="Old Title", description="Old Description", body={'old': 'data'})
    mock_session.query().filter().one_or_none.return_value = mock_project

    # Update the call to include new parameters
    result = project_gateway.update_project(1, new_title="Updated Title", new_description="Updated Description", new_body={'new': 'data'})

    assert result.title == "Updated Title"
    assert result.description == "Updated Description"
    assert result.body == {'new': 'data'}
    mock_session.commit.assert_called_once()


def test_delete_project(project_gateway, mock_session):
    """Test the delete_project method."""
    mock_project = Project(id=1, description="Test Project")
    mock_session.query().filter().one_or_none.return_value = mock_project

    result = project_gateway.delete_project(1)

    assert result is True
    mock_session.delete.assert_called_once()
    mock_session.commit.assert_called_once()
