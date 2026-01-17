from django.db import models
from django.contrib.auth.models import User


class Aula(models.Model):
    nombre = models.CharField(max_length=100)
    edificio = models.CharField(max_length=100, blank=True)
    tamaño = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return f"{self.nombre} ({self.edificio})" if self.edificio else self.nombre


class Carrera(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Clase(models.Model):
    nombre = models.CharField(max_length=200, blank=True)
    comision = models.CharField(max_length=50, blank=True)

    aula = models.ForeignKey(
        Aula,
        on_delete=models.CASCADE,
        related_name='clases'
    )

    carreras = models.ManyToManyField(
        Carrera,
        related_name='clases',
        blank=True
    )

    def __str__(self):
        base = self.nombre or "Clase"
        if self.comision:
            base += f" - Com. {self.comision}"
        return base


class Horario(models.Model):
    DIAS_SEMANA = [
        (0, 'Lunes'),
        (1, 'Martes'),
        (2, 'Miércoles'),
        (3, 'Jueves'),
        (4, 'Viernes'),
        (5, 'Sábado'),
    ]

    clase = models.ForeignKey(
        Clase,
        on_delete=models.CASCADE,
        related_name='horarios'
    )

    dia_semana = models.IntegerField(choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.get_dia_semana_display()} {self.hora_inicio}-{self.hora_fin}"


class Paso(models.Model):
    clase = models.ForeignKey(
        Clase,
        on_delete=models.CASCADE,
        related_name='pasos'
    )

    fecha = models.DateField()

    paso_quien = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pasos_realizados'
    )

    registrado_por = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pasos_registrados'
    )

    comentario = models.TextField(blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.clase} - {self.fecha}"
