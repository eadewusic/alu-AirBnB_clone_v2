#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage_type


class Amenity(BaseModel, Base):
    """This is the class for Amenity\
    Defines blueprint for Amenity objects and table schema
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    if storage_type == 'db':
        from models.place import place_amenity
        place_amenities = relationship("Place",
                                       secondary=place_amenity,
                                       back_populates="amenities")