from database import engine, Base
import model

Base.metadata.create_all(bind=engine)  # it would create all the tables mentioned in model.py