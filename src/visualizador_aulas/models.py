import peewee as pw


db = pw.SqliteDatabase('aulas.db')


class BaseModel(pw.Model):

    class Meta:
        database = db

class Aulas(BaseModel):
    asignatura = pw.CharField()
    turno = pw.CharField(null = True)
    dia = pw.CharField()
    fecha = pw.CharField(null= True)
    inicio = pw.TimeField()
    fin = pw.TimeField()
    pab = pw.IntegerField()
    aula = pw.CharField()
    pasamos = pw.BooleanField(default=False)


def models_db_connection():
    db.connect()
    db.create_tables([
        Aulas
        ])
    db.close()