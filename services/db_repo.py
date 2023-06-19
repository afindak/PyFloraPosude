from services.db_repo_init import session
from models.biljka import Biljka
from models.korisnik import Korisnik
from models.posuda import Posuda
from sqlalchemy import and_, func
from datetime import datetime as dt

def get_all_pybiljke()-> list[Biljka]:
    return (session.query(Biljka).all())

def get_pybiljke_by_id(id):
    return (session.query(Biljka)
              .filter(Biljka.id == id)
              .one_or_none())

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
            Posuda.naziv_lokacije == posuda.naziv_lokacije,
            Posuda.id_biljke == posuda.id_biljke))
            .one_or_none())
    if data is None:
        session.add(posuda)
        session.commit()

def update_pyposude(id, naziv_lokacije, id_biljke, vlaga_zemlje, ph_zemlje, razina_svjetla, temp_zraka):
    posuda_to_update = (session.query(Posuda)
                        .filter(Posuda.id == id)
                        .update({'naziv_lokacije': func.coalesce(naziv_lokacije, Posuda.naziv),
                                 'id_biljke': func.coalesce(id_biljke, Posuda.id_biljke),
                                 'vlaga_zemlje': func.coalesce(vlaga_zemlje, Posuda.vlaga_zemlje),
                                 'ph_zemlje': func.coalesce(ph_zemlje, Posuda.ph_zemlje),
                                 'razina_svjetla': func.coalesce(razina_svjetla, Posuda.razina_svjetla),
                                 'temp_zraka': func.coalesce(temp_zraka, Posuda.temp_zraka),
                                 'vrijeme_azuriranja': dt.now())
                        }))
    session.commit()
    return posuda_to_update
