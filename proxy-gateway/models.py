# Proxy Gateway - SQLAlchemy Database Models

#This model defines the structure of the db

from datetime import datetime
from typing import Optional # Optional is used to indicate that a field can be None, which is useful for fields that are not required
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, Index

from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy.sql import func

# The main class that our model will inherit from.
# This class provides the necessary functionality to define our database models and interact with the database using SQLAlchemy's ORM features.

from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base() # creating a base template for our models.

# defining out table as a class that inherits from Base.
class Metric(Base):
    # Name of the table in the db
    __tablename__ = "metrics"
    
    # the table colums (features)
    id = Column(Integer, primary_key=True)
    server_type = Column(String)
    metric_name = Column(String) # cpu_usage_percent, active_calls, etc.
    value = Column(Float)

# the pipline that connects to the db and allows us the interact with it.

DATABASE_URL = "postgresql://postgres:password@postgres:5432/telephony_db"
engine = create_engine(DATABASE_URL)

# Creating a session factory that will be used to create sessions for interacting with the db
SessionLocal = sessionmaker(bind=engine)

# When the cont starts for the first time, it will create the tables in the db if they do not exist.
# This is done by calling the create_tables function, which uses SQLAlchemy's metadata to create the tables based on the defined models.
def create_tables():
    Base.metadata.create_all(bind=engine)