from django.db import models

class userreg(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    passwrd = models.CharField(max_length=100)
    class Meta:
        db_table = "userreg"

class contact(models.Model):
    fname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phno = models.CharField(max_length=100)
    sub = models.CharField(max_length=100)
    msg = models.CharField(max_length=400)
    class Meta:
        db_table = "contact"
