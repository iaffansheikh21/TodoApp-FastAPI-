
from sqlmodel import SQLModel, create_engine # type: ignore
import os

connectionString = os.getenv('DB_URL')
engine = create_engine(connectionString)

def create_tables():
    SQLModel.metadata.create_all(engine)