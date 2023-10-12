from django.db import models

# Create your models here.
class msg(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=15)
    contact=models.CharField(max_length=12)
    sites=models.CharField(max_length=50)
    msg=models.CharField(max_length=50)
    class Meta:
        db_table='home_msg'