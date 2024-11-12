"""Write a program to transfer movies data in MongoDB cloud to SQLite database in local"""

import pandas as pd
import json
from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient


MONGODB_CONNECTION_STRING = "mongodb+srv://priyankak2088:MongodbPython123@cluster0.leza0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

if MONGODB_CONNECTION_STRING:

    
    DATABASE_URL = "sqlite:///sample_mflix.db"
    ENGINE = create_engine(DATABASE_URL, echo=True)
    BASE = declarative_base()
    SESSION_LOCAL = sessionmaker(bind=ENGINE)


    class Movies(BASE):
        __tablename__ = "movies"
        id = Column(String, primary_key=True)
        title = Column(String, nullable=True)
        cast = Column(Text, nullable=True)
        released = Column(Text, nullable=True)
        year = Column(Integer, nullable=True)
        rated = Column(String, nullable=True)


   
    BASE.metadata.create_all(ENGINE)

    session = SESSION_LOCAL()

    try:
        client = MongoClient(MONGODB_CONNECTION_STRING,tlsAllowInvalidCertificates=True)
        print("Connected to MongoDB.")

        
        database = client["sample_mflix"]
        collection = database["movies"]
        collection_data = collection.find().limit(100)

        for row in collection_data:
            
            new_movie = Movies(
                id=str(row.get("_id")),  
                title=row.get("title", ""),
                cast=json.dumps(row.get("cast", [])),   
                released=row.get("released", ""),   
                year=row.get("year", 0),
                rated=row.get("rated", "")
            )
            session.add(new_movie)
            session.commit()
        print("Data insertion completed.")

        movies = pd.DataFrame([movie.__dict__ for movie in session.query(Movies).all()])

        print(f"Movie details:\n{movies[['id', 'title', 'cast', 'released', 'year', 'rated']]}")

    except Exception as exception_msg:
        print(f"Exception: {exception_msg}")
else:
    print("MongoDB connection string is not configured")