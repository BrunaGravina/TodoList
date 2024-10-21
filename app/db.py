from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import redis


DATABASE_URL = "mysql://root:password@localhost/Todo"



# Configuração do Redis
REDIS_URL = "redis://localhost:3306"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


r = redis.Redis(host='localhost', port=3306, db=0)
