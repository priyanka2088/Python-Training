from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define database
database_url = "sqlite:///sqlalchemy.db"
engine = create_engine(database_url, echo=True)
base = declarative_base()
session_local = sessionmaker(bind=engine)


# Define simple ORM model
class User(base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)


# Create database & table
base.metadata.create_all(engine)

# Create a new session
session = session_local()

# Create new user in database
new_user = User(name="Damsel", age=18)
session.add(new_user)
session.commit()

# Reading from database
users = session.query(User).all()
print("User details:")
for user in users:
    print(user.id, user.name, user.age)

# Update data in database
user_to_update = session.query(User).filter_by(name="Bob").first()
if user_to_update:
    user_to_update.age = 99
    session.commit()

users = session.query(User).all()
print("User details after update:")
for user in users:
    print(user.id, user.name, user.age)

# Delete from database
user_to_delete = session.query(User).filter_by(name="Bob").first()
if user_to_delete:
    session.delete(user_to_delete)
    session.commit()

users = session.query(User).all()
print("User details after delete:")
for user in users:
    print(user.id, user.name, user.age)

session.close()
