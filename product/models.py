from django.db import models


# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=8)
    price=models.DecimalField(max_digits=350,decimal_places=2)
    description=models.TextField()



    def __str__(self):
        return self.name


class Produc(models.Model):
    nam=models.CharField(max_length=8)
    pric=models.DecimalField(max_digits=350,decimal_places=2)
    descriptio=models.TextField()
    def __str__(self):
        return self.nam

class Essaie(models.Model):
    image=models.ImageField()


