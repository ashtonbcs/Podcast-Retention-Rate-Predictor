from datetime import datetime
from sqlalchemy import BigInteger, Column, Float, DateTime, String, Text, Integer
from .base import Base

class Podcast(Base):
    __tablename__ = 'podcast_data'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    podcast_name = Column(Text)
    length_minutes = Column(Integer)
    intro_length_seconds = Column(Integer)
    adsNumber = Column(Integer)
    previous_ep_retention = Column(Integer)
    host_energy = Column(Integer)
    completion_percentage = Column(Integer)

    category = Column(Text)

class PodcastPrediction(Base):
    __tablename__ = 'podcast_prediction'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    podcast_name = Column(Text, nullable=False)
    length_minutes = Column(Integer, nullable=False)
    intro_length_seconds = Column(Integer, nullable=False)
    adsNumber = Column(Integer, nullable=False)
    previous_ep_retention = Column(Integer, nullable=False)
    host_energy = Column(Integer, nullable=False)
    pred_completion_percentage = Column(Integer, nullable=False)
