from services.db_repo_init import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, LargeBinary
from datetime import datetime as dt 
from constants import ENTITY_PRECISION, ENTITY_SCALE


class PyPosuda(Base):
    __tablename__ = 'pyposude'
    id = Column(Integer, primary_key=True, autoincrement=True)
    humidity = Column(Float(precision = ENTITY_PRECISION, scale= ENTITY_SCALE), nullable= False)
    ph = Column(Float(precision= ENTITY_PRECISION, scale = ENTITY_SCALE), nullable= False)
    temperature = Column(Float(precision= ENTITY_PRECISION, scale = ENTITY_SCALE), nullable= False)
    time_stamp = Column(DateTime, default= dt.now, nullable=False)

class PyBiljka(Base):
    __tablename__ = 'pybiljke'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable= False)
    image= Column(LargeBinary)
    def __repr__(self):
        return f'id = {self.id}, name = {self.name}'
    

