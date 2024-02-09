from django.db import models



class Hospital_Info(models.Model):
    name = models.CharField(max_length=100, verbose_name="Hospital's name")
    address = models.CharField(max_length=150, verbose_name='Address')
    phone_number = models.CharField(max_length=14, default='+2349012121212')
    email = models.EmailField()
    website = models.URLField()
    capacity = models.PositiveIntegerField()


    def __str__(self):
        return self.name
