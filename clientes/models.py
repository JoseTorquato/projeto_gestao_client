from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=2)
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    bio = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='cliente_photos', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
