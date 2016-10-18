import os

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session

Base = declarative_base()

class Station(Base):
    __tablename__ = 'station'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    types = relationship("Style",
                          backref='station',
                          cascade='all, delete-orphan')

    def __repr__(self):
        return "Station %s" % self.types

class Style(Base):
    __tablename__ = 'style'
    id = Column(Integer, primary_key=True)
    station_id = Column(Integer, ForeignKey('station.id'))
    name = Column(String(50))
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity':'style',
        'polymorphic_on':type
    }
    def __repr__(self):
        return "style of station %s" % self.name


engine = create_engine('sqlite://', echo=True)
Base.metadata.create_all(engine)

session = Session(engine)

s = Station(name='rack1')
session.add(s)
session.commit()

c = session.query(Station).get(1)
print c