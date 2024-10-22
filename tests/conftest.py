import sys
import os
from dotenv import load_dotenv
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base

# Adjust sys.path to include the project root directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Load environment variables from the .env file in the project root
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
load_dotenv(dotenv_path=dotenv_path)

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

    # Use sessionmaker to create a new session
    Session = sessionmaker(bind=connection)
    session = Session()

    yield session

    # Rollback the transaction and close the connection
    transaction.rollback()
    connection.close()