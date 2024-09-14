from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL ="postgresql://sit722_part3_afoj_user:Ypry7RpbjBpsjBiUHY3Y3jmpJcFEdokT@dpg-crij5ou8ii6s73f4fi8g-a.singapore-postgres.render.com/sit722_part3_afoj"   #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
