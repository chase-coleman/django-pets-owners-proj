from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

# owner class - name, age, number_of_pets
class Owner(models.Model):
  name = models.CharField(max_length=75, blank=False)
  age = models.IntegerField(null=False, default=False,validators=[MaxValueValidator(110), MinValueValidator(1)])
  number_of_pets = models.IntegerField(null=False, default=0)

# cat class - name, age, breed, vaccinated, description
class Cat(models.Model):
  name = models.CharField(max_length=75, blank=False)
  age = models.IntegerField(null=False, default=False,validators=[MaxValueValidator(30), MinValueValidator(1)])
  breed = models.CharField(max_length=50, blank=False)
  vaccinated = models.BooleanField(null=False, default=False)
  description = models.CharField(max_length=255, null=True, blank=True)
  
# bird class - name, age, species, vaccinated, description
class Bird(models.Model):
  name = models.CharField(max_length=75, blank=False)
  age = models.IntegerField(null=False, default=False,validators=[MaxValueValidator(30), MinValueValidator(1)])
  species = models.CharField(null=False, default=False, max_length=255)
  vaccinated = models.BooleanField(null=False, default=False)
  description = models.CharField(max_length=255, null=True, blank=True)  

# dog class - name, age, breed, vaccinated, description
class Dog(models.Model):
  name = models.CharField(max_length=75, blank=False)
  age = models.IntegerField(null=False, default=False,validators=[MaxValueValidator(30), MinValueValidator(1)])
  breed = models.CharField(max_length=50, blank=False)
  vaccinated = models.BooleanField(null=False, default=False)
  description = models.CharField(max_length=255, null=True, blank=True)

# exotic animal class - name, age, type_of_animal, vaccinated, region_of_origin
class Exotic_Animal(models.Model):
  name = models.CharField(max_length=75, blank=False)
  age = models.IntegerField(null=False, default=False,validators=[MaxValueValidator(30), MinValueValidator(1)])
  type_of_animal = models.CharField(max_length=50, blank=False)
  vaccinated = models.BooleanField(null=False, default=False)
  region_of_origin = models.CharField(max_length=255, null=True, blank=True)

