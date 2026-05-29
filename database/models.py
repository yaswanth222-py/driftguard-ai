from sqlalchemy import Column, Integer, Float, String
from database.db_config import Base

class PredictionLog(Base):

    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True, index=True)

    prediction = Column(Integer)

    confidence = Column(Float)

    status = Column(String)