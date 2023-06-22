from services.db_repo_init import db_init, session
from services.db_repo import insert_pybiljke, insert_pyposude, update_pybiljke, get_pybiljke_by_id, insert_korisnici
from models.biljka import Biljka
from models.posuda import Posuda
from models.korisnik import Korisnik
from services.data_simulation import save_sync_data, simul_data_for_pyposuda
from services.db_repo import get_user_by_username
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
    #biljka1 = get_pybiljke_by_id(1)
    #biljka1.add_image(path='C:\\Users\\afind\\Documents\\Python\\seminar_fotos\\macuhica.jpg')
    #update_pybiljke(1,None,biljka1.slika,None)
    #biljka1 = get_pybiljke_by_id(1)
    #biljka1.show_image()

    #posuda1 = Posuda('posuda_02', None, None, None, None, None)
    #insert_pyposude(posuda1)

    

    #vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla = simul_data_for_pyposuda()
    #save_sync_data(1, vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla)

    #print(vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla)
    #njega = get_njega(1)
    #print(njega)
    #for r in get_pyposude():
        #print(r.naziv)
   # korisnike = Korisnik('Ana', 'Findak', 'afindak', 'algebra1')
    #insert_korisnici(korisnike)
    user = get_user_by_username('afindak')
    print(user.ime)
    biljka2 = get_pybiljke_by_id(2)
    biljka2.show_image()