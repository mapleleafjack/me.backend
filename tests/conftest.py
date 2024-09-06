# conftest.py

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os

from db.models import Base

# Fixture for creating a SQLAlchemy engine connected to a test database
@pytest.fixture(scope='function')
def engine():
    # Use an environment variable or hardcoded connection string for the test database
    test_db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT', 5432)}/{os.getenv('DB_NAME')}_test"
    engine = create_engine(test_db_url)

    # Create the database tables
    Base.metadata.create_all(engine)

    yield engine

    # Drop the database tables after all tests in the session
    Base.metadata.drop_all(engine)


# Fixture for creating a SQLAlchemy session
@pytest.fixture(scope='function')
def session(engine):
    """Fixture to create a new database session for each test."""
    connection = engine.connect()

    # Begin a transaction
    transaction = connection.begin()

    # Create a configured "Session" class
    Session = sessionmaker(bind=connection)
    session = Session()

    yield session

    # Rollback the transaction after each test
    session.close()
    transaction.rollback()
    connection.close()
