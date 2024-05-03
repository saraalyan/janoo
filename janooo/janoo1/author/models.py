
from django.db import models

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    date_of_birth = models.DateField()
    date_of_death = models.DateField(blank=True, null=True)


