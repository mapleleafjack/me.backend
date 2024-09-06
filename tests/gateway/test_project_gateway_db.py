import pytest

from gateway.project_gateway import ProjectGateway

@pytest.fixture
def project_gateway(session):
    return ProjectGateway(db_session=session)

class TestProjectGatewayDB:
    def test_add_project(self, project_gateway):
        result = project_gateway.add_project("New Project")
        assert result.description == "New Project"

    def test_get_project(self, project_gateway):
        result = project_gateway.get_project(1)
        assert result is None

    def test_adds_and_gets_project(self, project_gateway):
        project_gateway.add_project("New Project")
        result = project_gateway.get_project(1)
        assert result.description == "New Project"