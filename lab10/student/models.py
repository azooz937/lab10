from django.db import models

class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Address2(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    addresses = models.ManyToManyField(Address2)

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title



