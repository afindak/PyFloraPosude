from services.db_repo_init import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from datetime import datetime as dt 
from constants import ENTITY_PRECISION, ENTITY_SCALE
from models.biljka import Biljka

class Posuda(Base):
    __tablename__ = 'pyposude'
    id = Column(Integer, primary_key=True, autoincrement=True)
    naziv = Column(String, nullable= True)
    vlaga_zemlje = Column(Float(precision = ENTITY_PRECISION, decimal_return_scale = ENTITY_SCALE), nullable= True)
    ph_zemlje = Column(Float(precision= ENTITY_PRECISION, decimal_return_scale = ENTITY_SCALE), nullable= True)
    temp_zraka = Column(Float(precision= ENTITY_PRECISION, decimal_return_scale = ENTITY_SCALE), nullable= True)
    razina_svjetla = Column(String, nullable= True)
    vrijeme_azuriranja = Column(DateTime, default= dt.now, nullable=True)
    id_biljke = Column(Integer, ForeignKey('pybiljke.id'), nullable= True  )
    
    def __init__(self, naziv, vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla, id_biljke):
        self.naziv = naziv
        self.vlaga_zemlje = vlaga_zemlje
        self.ph_zemlje = ph_zemlje
        self.temp_zraka = temp_zraka
        self.razina_svjetla = razina_svjetla
        self.vrijeme_azuriranja = dt.now()
        self.id_biljke = id_biljke