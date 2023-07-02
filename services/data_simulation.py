from random import uniform, randint, choice
import requests
from constants import URL
from models.biljka import Biljka
from services.db_repo import get_posuda_biljke, get_pyposude_by_id
from datetime import datetime
import json
import csv

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

def get_njega(posuda_id: int = None):
    njega = ''
    if posuda_id!= None:
        posuda =  get_pyposude_by_id(posuda_id)
        if posuda.ph_zemlje > 7:
            njega = 'Zakiseliti tlo, '
        elif posuda.ph_zemlje < 5.5:
            njega = 'Neutralizirati tlo, '
        if posuda.vlaga_zemlje > 50:
            njega = njega + 'isušiti tlo, '
        elif posuda.vlaga_zemlje < 30:
            njega = njega + 'zaliti tlo, '
        if posuda.razina_svjetla == 'niska':
            njega = njega + 'povećati svjetlost, '
        if posuda.temp_zraka < 10:
            njega = njega + 'preseliti na toplije '
        elif posuda.temp_zraka > 30:
            njega = njega + 'preseliti na hladnije '
    return njega

def save_sync_data(posuda_id, vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla):
    '''sync_data = dict()
    sync_data [f'{posuda_id}']= {'vlaga_zemlje': vlaga_zemlje,
                                 'ph_zemlje': ph_zemlje,
                                 'temp_zraka': temp_zraka,
                                 'razina_svjetla': razina_svjetla,
                                 'timestamp': str(datetime.now())}
    json.dump(sync_data, file_writer, indent=4)'''
    row = [posuda_id, vlaga_zemlje, ph_zemlje, temp_zraka, razina_svjetla]
    with open('db_data\pyposude.csv', 'a', encoding='UTF8', newline='') as file_writer:
        writer = csv.writer(file_writer)
        #header = ['vlaga_zemlje', 'ph_zemlje', 'temp_zraka', 'razina_svjetlosti', 'timestamp']
        #writer.writerow(header)
        writer.writerow(row)

        

