from services.db_repo_init import db_init
from services.db_repo import insert_pybiljke, insert_pyposude, update_pybiljke, get_pybiljke_by_id
from models.biljka import Biljka

if __name__== '__main__':
    db_init()
    '''biljka1= Biljka('Macuhica', 'svjetlo')
    #insert_pybiljke(biljka1)
    biljka1.add_image(path='C:\\Users\\afind\\Documents\\Python\\seminar_fotos\\macuhica.jpg')
    #update_pybiljke(1, None, slika, njega):
    insert_pybiljke(biljka1)

    biljka2= Biljka('Kaktus', 'svjetlo')
    biljka2.add_image(path= "C:\\Users\\afind\\Documents\\Python\\seminar_fotos\kaktus.jpg")
    insert_pybiljke(biljka2)'''
    #biljka2 = get_pybiljke_by_id(2)
    #biljka2.show_image()
    biljka1 = get_pybiljke_by_id(1)
    biljka1.add_image(path='C:\\Users\\afind\\Documents\\Python\\seminar_fotos\\macuhica.jpg')
    update_pybiljke(1,None,biljka1.slika,None)
    biljka1 = get_pybiljke_by_id(1)
    biljka1.show_image()


