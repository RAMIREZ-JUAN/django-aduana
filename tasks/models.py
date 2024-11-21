from django.db import models
from django.contrib.auth.models import User

# Create your models here.
impresoras = (
    ('hp', 'HP'),
    ('xr', 'XEROX'),
    ('ot', 'OTRO'),
)

scaners = (
    ('hp', 'HP'),
    ('ep', 'EPSON'),
    ('xr', 'XEROX'),
    ('fj', 'FUJITSU'),
    ('ot', 'OTRO'),
)

monitor=(
    ('smg','SAMSUNG'),
    ('hp','HP'),
    ('lg','LG'),
    ('dll','DELL'),
    ('bnq','BENQ'),
    ('ot','OTRO'),
)

disco=(
    ('dh','DISCO DURO'),
    ('sd','DISCO SOLIDO'),
)

cpu=(
    ('hp','HP'),
    ('dll','DELL'),
    ('ln','LENOVO'),
    ('lg','LG'),
    ('ot','otro'),
)

laptops=(
    ('hp','HP'),
    ('dll','DELL'),
    ('ac','ACER'),
    ('lnv','LENOVO'),
)

equipos = (
    ('CPU', 'Cpu'),
    ('MN', 'Monitor'),
    ('IP', 'Impresora'),
    ('SC', 'Scanner'),
    ('DC', 'Disco'),
)

unidades = (
    ('UA', 'Unida Administrativa'),
    ('UJ', 'Unidad Juridica'),
    ('UF', 'Unidad de Fiscalizacion'),
    ('AE', 'Aeropuerto El Alto'),
    ('PNL', 'Penal'),
    ('GYD', 'Gestion y Despachos'),
    ('SI', 'Secretaria Interior'),
    ('SG', 'Secretaria Gerencia'),
    ('VI', 'Ventanilla Interior'),
    ('VG', 'Ventanilla Gerencia'),
    ('CMS', 'Comisos'),
    ('UC', 'UCOE'),
    ('DP', 'Disposicon'),
    ('CC', 'Cobranza Coactiva'),
    ('AG', 'Archivos Gerencia'),
    ('AI', 'Archivos Interior'),
    ('TR', 'Transito'),
    ('PT', 'Plataforma'),
    ('SIS', 'Sistemas'),
    ('CBJ', 'Administracion Cobija'),
    ('CH', 'CHARAÑA'),
    ('DS', 'Desaguadero'),
    ('PH', 'PIA Huarina'),
    ('PG', 'PIA Guaqui'),
    ('PBJ', 'PIA Bojtilca'),
    ('PAA', 'PIA Achica Arriba'),
    ('PP', 'PIA Patacamaya'),
)


class Task(models.Model):
    nombre = models.CharField(max_length=200)
    unidad = models.CharField(choices=unidades, max_length=3, null=True)
    marca = models.CharField(choices=impresoras, max_length=2, null=True)
    marcas= models.CharField(choices=scaners,max_length=2, null= True)
    model=models.CharField(choices=laptops,max_length=3, null=True)
    cpu=models.CharField(choices=cpu,max_length=3,null=True)
    modelo= models.CharField(choices=monitor, max_length=3, null=True)
    tipo=models.CharField(choices=disco,max_length=3, null=True)
    codigo = models.CharField(max_length=50, null=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
