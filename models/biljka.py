from services.db_repo_init import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import backref, relationship
import base64
from io import BytesIO 
from PIL import Image

class Biljka(Base):
    __tablename__ = 'pybiljke'
    id = Column(Integer, primary_key=True, autoincrement=True)
    naziv = Column(String, nullable= False)
    slika = Column(String, nullable= True)
    njega = Column(String, nullable= True)
    posude = relationship('Posuda', backref=backref('biljka'))
    def __repr__(self):
        return f'id = {self.id}, name = {self.naziv}'
    def __init__(self, naziv, njega):
        self.naziv = naziv
        self.njega = njega 

    def add_image(self, path):
        try:
            image = open(path, 'rb') 
            try:
                image_read = image.read()
                image_64_encode = base64.b64encode(image_read)
            except:
                raise Exception('Something went wrong when encoding image')
        except:
                raise Exception('Something went wrong when opening image')
        image_encoded = image_64_encode.decode('utf-8')
        self.slika = image_encoded

    def show_image(self):
        file_slike = BytesIO(base64.decodebytes(bytes(self.slika, "utf-8")))
        foto = Image.open(file_slike).convert("RGB")
        foto.show() 

         