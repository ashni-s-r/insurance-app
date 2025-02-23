from sqlalchemy import Column, Integer, String

from models.db_base import Base


class Insurance_Model(Base):
    __tablename__ = 'insurance'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    premium = Column(String(255),  nullable=True)
    coverage = Column(String(255),  nullable=True)
