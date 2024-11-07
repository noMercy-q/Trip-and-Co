import enum

from sqlalchemy import Column, String, ForeignKey, Integer, Text, DateTime, Enum, JSON, DECIMAL
import uuid
from datetime import datetime

from sqlalchemy import Column, String, ForeignKey, Integer, Text, DateTime, UUID
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

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String)
    created_at = Column(DateTime, default=datetime.now())

class Trip(Base):
    __tablename__ = 'trips'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(Text)
    origin_city_id = Column(String, ForeignKey('cities.city_id'))
    dest_city_id = Column(String, ForeignKey('cities.city_id'))
    created_by = Column(UUID, ForeignKey('users.id'))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    created_at = Column(DateTime)

class TripItemsTypes(enum.Enum):
    hotel = "hotel"
    vehicle = "vehicle"
    view = "view"
class TripItem(Base):
    __tablename__ = "trip_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Enum(TripItemsTypes, name="tripitemstypes"), nullable=False)
    name = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    details = Column(JSON, nullable=True)
    cost = Column(DECIMAL, nullable=True)
    link_url = Column(Text, nullable=True)
    image_url = Column(Text, nullable=True)

