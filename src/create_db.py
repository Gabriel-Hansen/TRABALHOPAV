from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///mercado.db')
Base.metadat.create_all(engine)