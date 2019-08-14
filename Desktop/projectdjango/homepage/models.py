from django.db import models


class Homepage(models.Model):
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    title3 = models.CharField(max_length=200)
    title4 = models.CharField(max_length=200)
    title5 = models.CharField(max_length=200)
    title6 = models.CharField(max_length=200)
    description1 = models.CharField(max_length=200)
    description2 = models.CharField(max_length=200)
    description3 = models.CharField(max_length=200)
    description4 = models.CharField(max_length=200)
    description5 = models.CharField(max_length=200)
    description6 = models.CharField(max_length=200)
    photo1 = models.ImageField(upload_to='photos', blank=True)
    photo2 = models.ImageField(upload_to='photos', blank=True)
    photo3 = models.ImageField(upload_to='photos', blank=True)
    photo4 = models.ImageField(upload_to='photos', blank=True)
    photo5 = models.ImageField(upload_to='photos', blank=True)
    photo6 = models.ImageField(upload_to='photos', blank=True)

    def __str__(self):
        return self.title1
