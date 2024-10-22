from db.models import Project


class ProjectGateway:
    def __init__(self, db_session):
        # Use the session factory to get a new session
        self.session = db_session
    
    def get_project(self, project_id):
        """Retrieve a project by its ID."""
        try:
            # Query the database for the project with the given ID
            project = self.session.query(Project).filter(Project.id == project_id).one_or_none()
            return project
        except Exception as e:
            print(f"An error occurred while retrieving the project: {e}")
            return None
        
    def get_all_projects(self):
        """Retrieve all projects from the database."""
        try:
            # Query the database for all projects
            projects = self.session.query(Project).all()
            return projects
        except Exception as e:
            print(f"An error occurred while retrieving all projects: {e}")
            return None

    def add_project(self, title, description, body=None):
        """Add a new project to the database."""
        try:
            new_project = Project(title=title, description=description, body=body)
            self.session.add(new_project)
            self.session.commit()
            return new_project
        except Exception as e:
            print(f"An error occurred while adding the project: {e}")
            self.session.rollback()
            return None
        
    def update_project(self, project_id, new_title=None, new_description=None, new_body=None):
        """Update fields of an existing project."""
        try:
            project = self.session.query(Project).filter(Project.id == project_id).one_or_none()
            if project is not None:
                if new_title is not None:
                    project.title = new_title
                if new_description is not None:
                    project.description = new_description
                if new_body is not None:
                    project.body = new_body
                self.session.commit()
                return project
            else:
                print("Project not found")
                return None
        except Exception as e:
            print(f"An error occurred while updating the project: {e}")
            self.session.rollback()
            return None

    def delete_project(self, project_id):
        """Delete a project by its ID."""
        try:
            project = self.session.query(Project).filter(Project.id == project_id).one_or_none()
            if project is not None:
                self.session.delete(project)
                self.session.commit()
                return True
            else:
                print("Project not found")
                return False
        except Exception as e:
            print(f"An error occurred while deleting the project: {e}")
            self.session.rollback()
            return False
        
    def __del__(self):
        # Close the session when the object is destroyed
        self.session.close()