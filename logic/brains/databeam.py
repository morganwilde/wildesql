from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from logic.dbCredentials import database_0

# create the session
engine  = create_engine(str(database_0), pool_size = 20, max_overflow = 0)
session = sessionmaker(bind = engine)()