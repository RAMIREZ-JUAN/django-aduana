from django.db import models
from django.contrib.auth.models import User


# Create your models here.
disco=(
    ('dh','DISCO DURO'),
    ('sd','DISCO SOLIDO'),
)

equipos = (
    ('CPU', 'Cpu'),
    ('MN', 'Monitor'),
    ('IP', 'Impresora'),
    ('SC', 'Scanner'),
    ('DC', 'Disco'),
)

unidades = (
    ('Administrativa', 'Unida Administrativa'),
    ('Juridica', 'Unidad Juridica'),
    ('Fiscalizacion', 'Unidad de Fiscalizacion'),
    ('Aeropuerto', 'Aeropuerto El Alto'),
    ('Penal', 'Penal'),
    ('Gestion', 'Gestion'),
    ('Despachos', 'Despachos'),
    ('Secretaria Interior', 'Secretaria Interior'),
    ('Secretaria Gerencia', 'Secretaria Gerencia'),
    ('Ventanilla Interior', 'Ventanilla Interior'),
    ('Ventanilla Gerencia', 'Ventanilla Gerencia'),
    ('Comisos', 'Comisos'),
    ('Ucoe', 'UCOE'),
    ('Disposicion', 'Disposicon'),
    ('Coactiva', 'Cobranza Coactiva'),
    ('Archivos Gerencia', 'Archivos Gerencia'),
    ('Archivos Interior', 'Archivos Interior'),
    ('Transito', 'Transito'),
    ('Plataforma', 'Plataforma'),
    ('Sistemas', 'Sistemas'),
    ('Administracion Cobija', 'Administracion Cobija'),
    ('Charaña', 'Charaña'),
    ('Desaguadero', 'Desaguadero'),
    ('Huarina', 'PIA Huarina'),
    ('Guaqui', 'PIA Guaqui'),
    ('Bojtilaca', 'PIA Bojtilaca'),
    ('Achica Arriba', 'PIA Achica Arriba'),
    ('Patacamaya', 'PIA Patacamaya'),
)

class Task(models.Model):
    nombre = models.CharField(max_length=200)
    equipo = models.CharField(choices=equipos, max_length=3)
    unidad = models.CharField(choices=unidades, max_length=30)
    marca = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre