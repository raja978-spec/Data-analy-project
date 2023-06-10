from django.db import models
from datetime import datetime
# Create your models here.
class DashBoard(models.Model):
    Intensity=models.CharField(max_length=100,default='')
    Likehood=models.CharField(max_length=100,default='')
    Relevance=models.CharField(max_length=100,default='')
    SYear=models.CharField(max_length=100,default='')
    EYear=models.CharField(max_length=100,default='')
    Country=models.CharField(max_length=100,default='')
    Topic=models.CharField(max_length=100,default='')
    Region=models.CharField(max_length=100,default='')
    Url=models.CharField(max_length=100,default='')
    Added=models.CharField(max_length=100,default='')
    Published=models.CharField(max_length=100,default='')
    Insight=models.CharField(max_length=100,default='')
    
  