from django.db import models

class Breed(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100, choices=[('TINY', 'Tiny'),('SMALL','Small'),('MEDIUM','Medium'),('LARGE','Large')])
    friendliness = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])
    trainability = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])
    sheddingamount = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])
    exerciseneeds = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])

    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)

    def __str__(self):
        return self.name

