from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import yaml

# 各種設定読み込み
with open('config.yaml') as file:
  config = yaml.safe_load(file.read())
  username = config["database"]["springdbuser"]
  pw = config["database"]["springdbpw"]
  server = config["database"]["server"]

DATABASE = f'mysql+mysqlconnector://{username}:{pw}@{server}/springdb'

Engine = create_engine(
  DATABASE
)

Base = declarative_base()

Session = scoped_session(
  sessionmaker(
    autocommit=False,
    autoflush=True,
    bind=Engine    
  )
)

Base = declarative_base()
Base.query = Session.query_property()

