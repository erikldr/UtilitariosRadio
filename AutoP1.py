import os
from datetime import date
from shutil import copyfile

today = date.today()

if today.month < 10:
    pasta_do_dia = str(today.day) + '-0' + str(today.month) + '-' + str(today.year)
else:
    pasta_do_dia = str(today.day) + '-' + str(today.month) + '-' + str(today.year)
    
    
today = date.today().strftime("%A")

if today == 'Monday':
    dia_atual = '_SEGUNDA.mp3'
    
if today == 'Tuesday':
    dia_atual = '_TERCA.mp3'
    
if today == 'Wednesday':
    dia_atual = '_QUARTA.mp3'
    
if today == 'Thursday':
    dia_atual = '_QUINTA.mp3'

if today == 'Friday':
    dia_atual = '_SEXTA.mp3'
    
dir_atual = 'origem' + pasta_do_dia

destino1 = 'destino1'
destino2 = 'destino2'

programetes = os.listdir(dir_atual)

for i in range(len(programetes)):
    if programetes[i][-len(dia_atual):] == dia_atual:
        original = dir_atual + '\\' + programetes[i]
        
        maximus_dest = destino1 + programetes[i][:-len(dia_atual)] + '.mp3'
        paranaiba_dest = destino2 + programetes[i][:-len(dia_atual)] + '.mp3'
    
        copyfile(original, maximus_dest)
        copyfile(original, paranaiba_dest)