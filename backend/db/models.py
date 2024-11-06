from sqlalchemy import Column, String, ForeignKey
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
