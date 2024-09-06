from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)

    def serialize(self):
        """Return object data in easily serializable format."""
        return {
            'id': self.id,
            'description': self.description
        }