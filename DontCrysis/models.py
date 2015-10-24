from django.db import models
# Create your models here.
from django.db import models
default_report_id = 1
class Agency(models.Model):
    name = models.CharField(max_length=50)
    telephone=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=50, unique=True)
    type=models.IntegerField()
class Subscriber (models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=8)
    nric = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    postalcode = models.CharField(max_length=6)
    email = models.CharField(max_length=50, unique=True)
class Report(models.Model):
    type = models.IntegerField()
    date = models.DateField()
    text = models.CharField(max_length=500)
class ReportReceiver(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=20, unique=True)
class Crisis(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=150, null=True)
    postalcode = models.CharField(max_length=6)
    type = models.IntegerField()
    severity=models.IntegerField()
    date = models.DateTimeField()
    report = models.ForeignKey(Report)
    personName = models.CharField(max_length=30)
    personPhone = models.CharField(max_length=8)