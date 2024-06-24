import os
import logging

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker


load_dotenv()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

DATABASE_URL = f"postgresql+psycopg2://{os.getenv("DATABASE_USER")}:{os.getenv("DATABASE_PASSWORD")}@{os.getenv("DATABASE_ADDRESS")}:{os.getenv("DATABASE_PORT")}/{os.getenv("DATABASE")}"

engine = create_engine(DATABASE_URL, 
                        pool_size=20,
                        max_overflow=40,
                        pool_recycle=25200,
                        pool_timeout=30
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":

    try:
        with engine.connect() as connection:
            result = connection.execute(text('SELECT * FROM categories;'))
            data = result.fetchone()
            logger.info("Connection Success: Data Fetched: %s", data)

    except OperationalError as e:
        logger.error("Operational Error occurred: %s", e)

    except IntegrityError as e:
        logger.error("Integrity Error occurred: %s", e)

    except SQLAlchemyError as e:
        logger.error("General SQLAlchemy Error occurred: %s", e)

    except Exception as e:
        logger.error("An unexpected error occurred: %s", e)
        