from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://projectLeonisa:123456@localhost:5432/projectLeonisa"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)