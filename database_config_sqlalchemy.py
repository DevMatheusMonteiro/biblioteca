import os
import sqlalchemy as sql
import sqlalchemy.orm as orm

engine = sql.create_engine(f"sqlite:///{os.getcwd()}\\database.db")
Base = orm.declarative_base()
Session = orm.sessionmaker(bind=engine)
session = Session()

def create_tables():
    Base.metadata.create_all(engine)