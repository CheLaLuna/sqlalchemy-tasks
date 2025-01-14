from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Director
import os
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# BEGIN (write your solution here)
def delete_director(session, director_id):
    director = (session.query(Director).filter(director_id == Director.id).first())
    if director:
        session.delete(director)
        session.commit()
        print(f"Director with ID {director_id} and their movies have been deleted.")
    else:
        session.rollback()
        print(f"Director with ID {director_id} not found.")
# END
