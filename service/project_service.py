from db.models import Project

def add_project(description: str, session) -> Project:
    """Add a new project to the database."""
    new_project = Project(description=description)
    session.add(new_project)
    session.commit()
    return new_project

def get_projects(session):
    """Retrieve all projects from the database."""
    return session.query(Project).all()

def delete_projects(session):
    """Delete all projects from the database."""
    session.query(Project).delete()
    session.commit()
    return True