from sqlalchemy import Column, Integer, String
from app.database import Base

class Campaign(Base):
    __tablename__ = "campaigns"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    goal = Column(String)
    platform = Column(String)
