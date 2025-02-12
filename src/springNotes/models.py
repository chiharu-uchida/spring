from sqlalchemy import Column, Integer, String, Float, DateTime
from mysql_setting import Engine
from mysql_setting import Base

class User(Base):
    """
    ユーザー
    """

    __tablename__ = 'spring_user'
    __table_args__ = {
        'comment': 'ユーザー情報を管理'
    }

    user_id = Column('user_id', Integer, primary_key=True, autoincrement=True)
    user_name = Column('user_name', String(200))
    updated_date = Column('updated_date', DateTime)
    registration_date = Column('registration_date', DateTime)

class Note(Base):
    """
    メモ
    """

    __tablename__ = 'note'
    __table_args__ = {
        'comment': 'メモの情報と内容を管理'
    }

    note_id = Column('note_id', Integer, primary_key=True, autoincrement=True)
    note_name = Column('note_name', String(100))
    creator = Column('creator', Integer)
    contents = Column('contents', String(10000))
    updated_date = Column('updated_date', DateTime)
    registration_date = Column('registration_date', DateTime)


if __name__ == "__main__":
    Base.metadata.create_all(bind=Engine)