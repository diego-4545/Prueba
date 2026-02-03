import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("postgresql://pruebaa_onlk_user:U0nqQV6DrKlGw707RmudYR4v6nimLhAv@dpg-d60n87l6ubrc739b1hh0-a/pruebaa_onlk")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
