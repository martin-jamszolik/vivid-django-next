from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=100,default='Draft')

class Proposal(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    prop_type = models.IntegerField(default=0)
