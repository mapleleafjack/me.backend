from db.models import Project


def test_create_project(session):
    """Test creating a new project."""
    # Add a new project
    new_project = Project(description='Test project')
    session.add(new_project)
    session.commit()

    # Query the database to check if the project was added
    project = session.query(Project).filter_by(description='Test project').first()

    assert project is not None
    assert project.description == 'Test project'