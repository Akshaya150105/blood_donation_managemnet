from django.db import models

# Create your models here.
class User(models.Model):
    uid=models.CharField(max_length=20,primary_key=True)
    uname=models.CharField(max_length=100)
    uemail=models.EmailField()
    ucontact=models.CharField(max_length=10)
    ublood=models.CharField(max_length=5)
    class Meta:
        db_table="user"
    