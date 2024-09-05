from db.models import Project
from service.project_service import add_project, delete_projects, get_projects

def test_add_project(session):
    """Test the add_project function."""
    description = 'New Project'
    
    # Call the add_project function with the session
    new_project = add_project(description, session)
    
    # Check if the project was added
    assert new_project is not None
    assert new_project.description == description
    
    # Verify that the project is in the database
    stored_project = session.query(Project).filter_by(description=description).first()
    assert stored_project is not None
    assert stored_project.description == description

def test_get_projects(session):
    """Test the get_projects function."""
    description1 = 'Project 1'
    description2 = 'Project 2'
    
    # Add projects using the add_project function with the session
    add_project(description1, session)
    add_project(description2, session)
    
    # Call the get_projects function with the session
    projects = get_projects(session)
    
    # Check if the projects were retrieved
    assert len(projects) >= 2
    descriptions = {project.description for project in projects}
    assert description1 in descriptions
    assert description2 in descriptions

def test_delete_projects(session):
    """Test the delete_projects function."""
    description = 'Project to delete'
    
    # Add a project using the add_project function with the session
    add_project(description, session)
    
    # Call the delete_projects function with the session
    delete_projects(session)
    
    # Verify that the project was deleted
    project = session.query(Project).filter_by(description=description).first()
    assert project is None