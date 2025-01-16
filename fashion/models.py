from django.db import models

# Create your models here.
class fashionCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    #image = models.ImageField(upload_to='fashionCategory/')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

