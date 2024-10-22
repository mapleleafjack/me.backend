from db.models import Project


def test_project(session):
    """Test creating a new project."""
    # Add a new project
    new_project = Project(title='Test Title', description='Test project', body={'key': 'value'})
    session.add(new_project)
    session.commit()

    # Query the database to check if the project was added
    project = session.query(Project).filter_by(title='Test Title').first()

    assert project is not None
    assert project.title == 'Test Title'
    assert project.description == 'Test project'
    assert project.body == {'key': 'value'}

    # Delete the project
    session.delete(project)
    session.commit()

    # Query the database to check if the project was deleted
    project = session.query(Project).filter_by(title='Test Title').first()

    assert project is None
