from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)       
    description = Column(String, nullable=False)
    body = Column(JSON, nullable=True) 

    def serialize(self):
        """Return object data in easily serializable format."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'body': self.body
        }
