import unittest

from usecase.project_usecase import ProjectUseCase

class MockProjectGateway:
    """Mock data gateway for testing purposes."""
    def __init__(self):
        self.projects = {}
        self.next_id = 1

    def get_project(self, project_id):
        return self.projects.get(project_id, None)

    def add_project(self, description):
        project_id = self.next_id
        self.projects[project_id] = {'id': project_id, 'description': description}
        self.next_id += 1
        return self.projects[project_id]

    def update_project(self, project_id, new_description):
        if project_id in self.projects:
            self.projects[project_id]['description'] = new_description
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
        self.mock_gateway.add_project("Initial project")

        # Test
        project = self.use_case.get_project(1)

        # Assert
        self.assertIsNotNone(project)
        self.assertEqual(project['id'], 1)
        self.assertEqual(project['description'], "Initial project")

    def test_add_project(self):
        # Test
        new_project = self.use_case.add_project("New project")

        # Assert
        self.assertIsNotNone(new_project)
        self.assertEqual(new_project['id'], 1)
        self.assertEqual(new_project['description'], "New project")

    def test_update_project(self):
        # Setup
        self.mock_gateway.add_project("Initial project")

        # Test
        updated_project = self.use_case.update_project(1, "Updated project")

        # Assert
        self.assertIsNotNone(updated_project)
        self.assertEqual(updated_project['id'], 1)
        self.assertEqual(updated_project['description'], "Updated project")

    def test_delete_project(self):
        # Setup
        self.mock_gateway.add_project("Project to delete")

        # Test
        deleted_project = self.use_case.delete_project(1)

        # Assert
        self.assertIsNotNone(deleted_project)
        self.assertEqual(deleted_project['id'], 1)
        self.assertEqual(deleted_project['description'], "Project to delete")

        # Verify that the project was actually removed
        self.assertIsNone(self.mock_gateway.get_project(1))