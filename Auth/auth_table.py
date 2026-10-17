from Auth.auth_database import engine, Base
from Auth import models  

Base.metadata.create_all(bind=engine)  # it would create all the tables mentioned in model.py