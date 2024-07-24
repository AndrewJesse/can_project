from sqlalchemy import Column, Integer, String
from .database import Base

class CANMessage(Base):
    __tablename__ = 'can_messages'

    id = Column(Integer, primary_key=True, index=True)
    arbitration_id = Column(String(255), index=True)  # Specify the length
    data = Column(String(255))  # Specify the length
