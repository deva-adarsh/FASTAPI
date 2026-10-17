from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, declarative_base

MYSQL_USER = "root"
MYSQL_PASSWORD = "Triumph@400"
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_DATABASE = "fastapi_db"

DATABASE_URL = URL.create(
    "mysql+pymysql",
    username=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    database=MYSQL_DATABASE,
)
#establish the connection
engine = create_engine(DATABASE_URL)

#This line of code make the session to start
SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

# ThIS FUNCTION MAKES THE session to stop 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()