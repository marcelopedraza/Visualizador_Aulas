import csv
from datetime import time
from src.visualizador_aulas.models import Aulas,models_db_connection

models_db_connection()

def timear(hora):
    #import pdb; pdb.set_trace()
    return hora.split(':')
    
with open('test_viernes.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        aula = Aulas()
        aula.asignatura = row[0]
        aula.turno = row[1]
        aula.dia = row[3]
        aula.fecha = row[4]
        aula.inicio = time(int(timear(row[5])[0]),int(timear(row[5])[1]))
        aula.fin = time(int(timear(row[6])[0]),int(timear(row[6])[1]))
        aula.pab = row[7]
        aula.aula = row[8]
        aula.save()
