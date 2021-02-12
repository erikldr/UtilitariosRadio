import os
from datetime import date
from shutil import copyfile

today = date.today().strftime("%A")

if today == 'Monday':
    dia_atual = 'LLI-SEG'
    
if today == 'Tuesday':
    dia_atual = 'LLI-TER'
    
if today == 'Wednesday':
    dia_atual = 'LLI-QUA'
    
if today == 'Thursday':
    dia_atual = 'LLI-QUI'

if today == 'Friday':
    dia_atual = 'LLI-SEX'
    
dir_ll = 'origem'
maximus = 'destino'

programetes = os.listdir(dir_ll)

for i in range(len(programetes)):
    if programetes[i][:len(dia_atual)] == dia_atual:
        if len(programetes[i]) <= 13:
            if len(programetes[i]) == 13:
                nome = 'LEAO LOBO FOFOCA ' + programetes[i][len(dia_atual):]
            else:
                nome = 'LEAO LOBO FOFOCA 0' + programetes[i][len(dia_atual):]
        else:
            if len(programetes[i]) == 19:
                nome = 'LEAO LOBO ANIVERSARIO.mp3'
        
            else:
                nome = 'LEAO LOBO NOVELA 0' + programetes[i][len(dia_atual) + 1:-11] + '.mp3'
            
        original = dir_ll + '\\' + programetes[i]
        
        maximus_dest = maximus + nome
    
        copyfile(original, maximus_dest)