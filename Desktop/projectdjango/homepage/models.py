from django.db import models


class Hompeage(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    photo1 = models.ImageField(upload_to='photos', blank=True)
    photo2 = models.ImageField(upload_to='photos', blank=True)
    photo3 = models.ImageField(upload_to='photos', blank=True)
    photo4 = models.ImageField(upload_to='photos', blank=True)
    photo5 = models.ImageField(upload_to='photos', blank=True)
    photo6 = models.ImageField(upload_to='photos', blank=True)

    def __str__(self):
        return self.title
