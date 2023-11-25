from django.db import models

# Create your models here.


class AddressDetails(models.Model):
    """ Creating AddressDetails model"""
    houseno = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)


class WorkExperience(models.Model):
    """ Creating WorkExperience model"""
    companyName = models.CharField(max_length=100)
    fromDate = models.DateField()
    toDate = models.DateField()
    address = models.TextField()


class Qualification(models.Model):
    """ Creating Qualification model"""
    qualificationName = models.CharField(max_length=100)
    percentage = models.FloatField()


class Project(models.Model):
    """ Creating Project model"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.TextField()  # Storing Base64 encoded image as text field


class Employee(models.Model):
    """ Creating Employee model"""
    regid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phoneNo = models.CharField(max_length=20)
    addressDetails = models.OneToOneField(AddressDetails, on_delete=models.CASCADE)
    workExperience = models.ManyToManyField(WorkExperience)
    qualifications = models.ManyToManyField(Qualification)
    projects = models.ManyToManyField(Project)
