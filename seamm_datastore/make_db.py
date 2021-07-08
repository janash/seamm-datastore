"""
Functions for connection to database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from .models import Base

def connect(database_uri, initialize=False):

    engine = create_engine(database_uri)
    db_session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )

    if initialize:
        Base.metadata.drop_all(engine)

    Base.metadata.create_all(engine)
    Base.query = db_session.query_property()

    return db_session