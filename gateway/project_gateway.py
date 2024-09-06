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

    def add_project(self, description):
        """Add a new project to the database."""
        try:
            # Create a new project instance
            new_project = Project(description=description)
            self.session.add(new_project)
            self.session.commit()
            return new_project
        except Exception as e:
            print(f"An error occurred while adding the project: {e}")
            self.session.rollback()
            return None
        
    def update_project(self, project_id, new_description):
        """Update the description of an existing project."""
        try:
            project = self.session.query(Project).filter(Project.id == project_id).one_or_none()
            if project is not None:
                project.description = new_description
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