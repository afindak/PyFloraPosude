from services.db_repo_init import session
from models.biljka import Biljka
from models.korisnik import Korisnik
from models.posuda import Posuda
from sqlalchemy import and_, func
from datetime import datetime as dt

def get_user_by_username(username):
    return (session.query(Korisnik)
            .filter(Korisnik.username == username)
            .one_or_none())

def get_all_pybiljke()-> list[Biljka]:
    return (session.query(Biljka).all())

def get_pybiljke_by_id(id):
    return (session.query(Biljka)
              .filter(Biljka.id == id)
              .one_or_none())

def get_pyposude(all_pyposude : bool = False) -> list[Posuda]:
    if not all_pyposude:
        query = (session.query(Posuda)
            .join(Biljka)
            .filter(Posuda.id_biljke is not None ))
    else:
        query = (session.query(Posuda)
            .outerjoin(Biljka))
    return query.all() 
             
def get_posuda_biljke(biljka_id: Biljka.id):
    return (session.query(Biljka) #.select_from(Biljka)
            .join(Posuda) #Posuda)
            .filter(Biljka.id == biljka_id)
            .all())

def insert_korisnici(korisnik: Korisnik):
    data = (session.query(Korisnik)
              .filter(and_(Korisnik.ime == korisnik.ime,
                           Korisnik.prezime == korisnik.prezime))
              .one_or_none())
    if data is None:
        session.add(korisnik)
        session.commit()

def insert_pybiljke(biljka: Biljka):
    data = (session.query(Biljka)
              .filter(Biljka.naziv == biljka.naziv)
              .one_or_none())
    if data is None:
        session.add(biljka)
        session.commit()

def update_pybiljke(id, naziv, slika, njega):
    biljka_to_upd = (session.query(Biljka)
                     .filter(Biljka.id == id)
                     .update({'naziv': func.coalesce(naziv, Biljka.naziv),
                              'slika': func.coalesce(slika, Biljka.slika),
                              'njega': func.coalesce(njega, Biljka.njega)}))
    session.commit()
    return biljka_to_upd

def delete_pybiljke(biljka_to_del: Biljka):
    session.delete(biljka_to_del)
    session.commit()

def insert_pyposude(posuda: Posuda):
    data = (session.query(Posuda)
            .filter(and_(
            Posuda.naziv == posuda.naziv,
            Posuda.id_biljke == posuda.id_biljke))
            .one_or_none())
    if data is None:
        session.add(posuda)
        session.commit()

def update_pyposude(id, naziv, vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla, id_biljke):
    posuda_to_update = (session.query(Posuda)
                        .filter(Posuda.id == id)
                        .update({'naziv': func.coalesce(naziv, Posuda.naziv),
                                 'vlaga_zemlje': func.coalesce(vlaga_zemlje, Posuda.vlaga_zemlje),
                                 'ph_zemlje': func.coalesce(ph_zemlje, Posuda.ph_zemlje),
                                 'temp_zraka': func.coalesce(temp_zraka, Posuda.temp_zraka),
                                 'razina_svjetla': func.coalesce(razina_svjetla, Posuda.razina_svjetla),
                                 'vrijeme_azuriranja': dt.now(),
                                 'id_biljke': func.coalesce(id_biljke, Posuda.id_biljke)})
                        )
    session.commit()
    return posuda_to_update

def delete_pyposude(posuda_to_del: Posuda):
    session.delete(posuda_to_del)
    session.commit()
 