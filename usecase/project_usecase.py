class ProjectUseCase:
    def __init__(self, project_gateway):
        self.project_gateway = project_gateway
    
    def get_project(self, project_id):
        """Retrieve a project by its ID."""
        return self.project_gateway.get_project(project_id)
    
    def get_all_projects(self):
        """Retrieve all projects from the database."""
        return self.project_gateway.get_all_projects()
    
    def add_project(self, description):
        """Add a new project to the database."""
        return self.project_gateway.add_project(description)
    
    def update_project(self, project_id, new_description):
        """Update the description of an existing project."""
        return self.project_gateway.update_project(project_id, new_description)
    
    def delete_project(self, project_id):
        """Delete a project by its ID."""
        return self.project_gateway.delete_project(project_id)