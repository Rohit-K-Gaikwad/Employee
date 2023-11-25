from rest_framework import serializers
from .models import Employee, AddressDetails, WorkExperience, Qualification, Project


class AddressDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressDetails
        fields = ('houseno', 'street', 'city', 'state')


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ('companyName', 'fromDate', 'toDate', 'address')


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ('qualificationName', 'percentage')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'description', 'photo')


class EmployeeSerializer(serializers.ModelSerializer):
    addressDetails = AddressDetailsSerializer()
    workExperience = WorkExperienceSerializer(many=True)
    qualifications = QualificationSerializer(many=True)
    projects = ProjectSerializer(many=True)

    class Meta:
        model = Employee
        fields = ('name', 'email', 'age', 'gender', 'phoneNo', 'addressDetails', 'workExperience', 'qualifications', 'projects')
