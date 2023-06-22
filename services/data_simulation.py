from random import uniform, randint, choice
import requests
from constants import URL
from models.biljka import Biljka
from services.db_repo import get_posuda_biljke, get_pyposude
from datetime import datetime
import json

def get_temperature()-> float:
    response = requests.get(URL)
    weather_data = response.json()
    return weather_data['current_weather']['temperature']

def simul_data_for_pyposuda()-> tuple[int, float, float, str]:
    vlaga_zemlje = randint(5, 90) #30-50
    ph_zemlje = round(uniform(3,9), 2) #5.5-7
    temp_zraka = get_temperature()
    razina_svjetla = choice(['visoka', 'niska', 'srednja'])
    return vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla

def get_njega(biljka_id: int):
    njega = ''
    for biljka in get_posuda_biljke(biljka_id):
        for r in biljka.posude:
            if r.ph_zemlje > 7:
                njega = 'Zakiseliti tlo, '
            elif r.ph_zemlje < 5.5:
                njega = 'Neutralizirati tlo, '
            if r.vlaga_zemlje > 50:
                njega = njega + 'isušiti tlo, '
            elif r.vlaga_zemlje < 30:
                njega = njega + 'zaliti tlo, '
            if r.razina_svjetla == 'niska':
                njega = njega + 'povećati svjetlost, '
            if r.temp_zraka < 10:
                njega = njega + 'preseliti na toplije '
            elif r.temp_zraka > 30:
                njega = njega + 'preseliti na hladnije '
    return njega

def save_sync_data(posuda_id, vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla):
    sync_data = dict()
    sync_data [f'{posuda_id}']= {'vlaga_zemlje': vlaga_zemlje,
                                 'ph_zemlje': ph_zemlje,
                                 'temp_zraka': temp_zraka,
                                 'razina_svjetla': razina_svjetla,
                                 'timestamp': str(datetime.now())}
    with open('db_data\pyposude.txt', 'a') as file_writer:
        json.dump(sync_data, file_writer, indent=4)
