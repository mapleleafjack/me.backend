import unittest

from usecase.project_usecase import ProjectUseCase

class MockProjectGateway:
    """Mock data gateway for testing purposes."""
    def __init__(self):
        self.projects = {}
        self.next_id = 1

    def get_project(self, project_id):
        return self.projects.get(project_id, None)

    def add_project(self, title, description, body=None):
        project_id = self.next_id
        self.projects[project_id] = {'id': project_id, 'title': title, 'description': description, 'body': body}
        self.next_id += 1
        return self.projects[project_id]

    def update_project(self, project_id, new_title=None, new_description=None, new_body=None):
        if project_id in self.projects:
            if new_title is not None:
                self.projects[project_id]['title'] = new_title
            if new_description is not None:
                self.projects[project_id]['description'] = new_description
            if new_body is not None:
                self.projects[project_id]['body'] = new_body
            return self.projects[project_id]
        return None

    def delete_project(self, project_id):
        return self.projects.pop(project_id, None)

class TestProjectUseCase(unittest.TestCase):
    def setUp(self):
        self.mock_gateway = MockProjectGateway()
        self.use_case = ProjectUseCase(self.mock_gateway)

    def test_get_project(self):
        # Setup
        self.mock_gateway.add_project("Initial project", "Initial description")

        # Test
        project = self.use_case.get_project(1)

        # Assert
        self.assertIsNotNone(project)
        self.assertEqual(project['id'], 1)
        self.assertEqual(project['title'], "Initial project")
        self.assertEqual(project['description'], "Initial description")

    def test_update_project(self):
        # Setup
        self.mock_gateway.add_project("Initial project", "Initial description")

        # Test
        updated_project = self.use_case.update_project(1, new_title="Updated project", new_description="Updated description")

        # Assert
        self.assertIsNotNone(updated_project)
        self.assertEqual(updated_project['id'], 1)
        self.assertEqual(updated_project['title'], "Updated project")
        self.assertEqual(updated_project['description'], "Updated description")


    def test_add_project(self):
        # Test
        new_project = self.use_case.add_project("Test Title", "New project", {"key": "value"})

        # Assert
        self.assertIsNotNone(new_project)
        self.assertEqual(new_project['id'], 1)
        self.assertEqual(new_project['title'], "Test Title")
        self.assertEqual(new_project['description'], "New project")
        self.assertEqual(new_project['body'], {"key": "value"})

    def test_delete_project(self):
        # Setup
        self.mock_gateway.add_project("Project to delete", "Description of project to delete")

        # Test
        deleted_project = self.use_case.delete_project(1)

        # Assert
        self.assertIsNotNone(deleted_project)
        self.assertEqual(deleted_project['id'], 1)
        self.assertEqual(deleted_project['title'], "Project to delete")
        self.assertEqual(deleted_project['description'], "Description of project to delete")
