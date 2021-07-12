from django.db import models

# Create your models here.
class data(models.Model):
    hostname=models.CharField(max_length=50)
    ip_address=models.GenericIPAddressField()
    date_time=models.TimeField(auto_now=False, auto_now_add=False,)
    n=models.IntegerField()
    def __str__(self):
        return self.hostname
