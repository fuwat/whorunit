from django.db import models


# Create your models here.
class Cpu(models.Model):
    speed = models.CharField(max_length=20)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)


class Ram(models.Model):
    size = models.CharField(max_length=20)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)


class Amd(models.Model):
    name = models.CharField(max_length=10)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)


class Nvidia(models.Model):
    name = models.CharField(max_length=10)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)


class Game(models.Model):
    name = models.CharField(max_length=20)
    img = models.URLField()
    release = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    info = models.CharField(max_length=200)
    cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE)
    ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    amd = models.ForeignKey(Amd, on_delete=models.CASCADE)
    nvidia = models.ForeignKey(Nvidia, on_delete=models.CASCADE)
