# -*- coding: utf-8 -*-
from django.db import models

#Choices for a 'tipo'
TIPOS           = (
                ('Automovil', 'Automovil'),
                ('Camioneta', 'Camioneta'),
                ('Camiones', 'Camiones'),
    )

class Categoria(models.Model):
    
    tipo        = models.CharField(max_length=10, choices=TIPOS)
    def __unicode__(self):
        return self.tipo


#Choices for a 'modelo'
CLASES = (
    ('vt', 'VENTUS'),
    ('dp', 'DYNAPRO'),
    ('op', 'OPTIMO'),
    ('ra08', 'RA08'),
    ('tbr', 'TBR'),

)


class Disenho(models.Model):
    modelo = models.CharField(max_length=10, choices=CLASES)

    def __unicode__(self):
        return self.modelo


class Medidas(models.Model):
    altura = models.IntegerField()
    aro = models.DecimalField(max_digits=5, decimal_places=2)
    ancho = models.IntegerField()

    def __unicode__(self):
        return str(self.ancho)


class Neumatico(models.Model):
    nombre = models.CharField(max_length=200)
    disenho = models.ForeignKey(Disenho)
    categoria = models.ForeignKey(Categoria)
    medidas = models.ForeignKey(Medidas)
    image = models.ImageField(upload_to='pictures', blank=True)

    def __unicode__(self):
        return self.nombre

class Personal(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tel_numb = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    twitter = models.CharField(max_length=30,blank=True)
    def __unicode__(self):
        return self.nombre


