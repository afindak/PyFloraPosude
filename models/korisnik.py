from services.db_repo_init import Base
from sqlalchemy import Column, Integer, String, Boolean

class Korisnik(Base):
    __tablename__ = 'pykorisnici'
    id = Column(Integer, primary_key= True, autoincrement= True)
    ime = Column(String, nullable= False )
    prezime = Column(String, nullable= False)
    username = Column(String, nullable= False)
    password = Column(String, nullable= False)

    def __init__(self, ime, prezime, username, password):
        self.ime = ime
        self.prezime = prezime
        self.username = username
        self.password = password
        #self.is_logged_in = is_logged_in
        
