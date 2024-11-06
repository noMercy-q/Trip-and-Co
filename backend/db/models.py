from sqlalchemy import Column, String, ForeignKey, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'

    city_id = Column(String(10), primary_key=True)
    city_name = Column(String(100))


class Airport(Base):
    __tablename__ = 'airports'

    airport_id = Column(String(10), primary_key=True)
    airport_name = Column(String(100))
    city_id = Column(String(10), ForeignKey('cities.city_id'))

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String)
    created_at = Column(DateTime)

class Trip(Base):
    __tablename__ = 'trips'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(Text)
    origin_city_id = Column(String, ForeignKey('cities.city_id'))
    dest_city_id = Column(String, ForeignKey('cities.city_id'))
    created_by = Column(Integer, ForeignKey('users.id'))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    created_at = Column(DateTime)
