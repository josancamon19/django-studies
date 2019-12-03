from django.db import models
from django.utils.timezone import now

# Create your models here.
class Company(models.Model):  # company.programmer_set.all() returns all programmers in this company
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    date_created = models.DateField(default=now())

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20)
    creator = models.CharField(max_length=20)
    paradigm = models.CharField(max_length=20)
    date_created = models.DateField(default=now())

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
