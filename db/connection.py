from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Retrieve configuration from environment variables
postgresql_db_endpoint = os.getenv("DB_HOST")
postgresql_db_port = os.getenv("DB_PORT", 5432)
postgresql_db_name = os.getenv("DB_NAME")
postgresql_db_user = os.getenv("DB_USER")
postgresql_db_password = os.getenv("DB_PASSWORD")

# Create SQLAlchemy engine
def get_db_engine():
    """Function to create SQLAlchemy engine."""
    engine_url = f"postgresql://{postgresql_db_user}:{postgresql_db_password}@{postgresql_db_endpoint}:{postgresql_db_port}/{postgresql_db_name}"
    return create_engine(engine_url)

def check_db_connection():
    """Function to check the connection to the PostgreSQL database using SQLAlchemy."""
    logging.info('Checking database connection')
    
    engine = get_db_engine()

    try:
        # Test the connection by executing a simple query
        with engine.connect() as connection:
            result = connection.execute("SELECT 1")
            logging.info('Database connection successful')
            return True
    except OperationalError as e:
        logging.error(f"Database connection failed: {e}")
        return False
