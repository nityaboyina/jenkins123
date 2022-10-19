from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms 
 
# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_hod = models.BooleanField('Is HOD', default=False)
    is_staff = models.BooleanField('Is STAFF', default=False)
class excel_file(models.Model):
    S_No = models.CharField(max_length=10, null=True)
    RollNo = models.CharField(max_length=15,null=True)
    Name = models.CharField(max_length=100,null=True)  

    GradeR = models.CharField(max_length=100,null=True)
    PointsR = models.CharField(max_length=30,null=True)
    CreditsR = models.CharField(max_length=12, default='',null=True)
    Resc = models.CharField(max_length=500, default='',null=True)

    GradeW = models.CharField(max_length=100,null=True)
    PointsW = models.CharField(max_length=30,null=True)
    CreditsW = models.CharField(max_length=12, default='',null=True)
    web_tech= models.CharField(max_length=500, default='',null=True) 

    GradeD = models.CharField(max_length=100,null=True)
    PointsD = models.CharField(max_length=30,null=True)
    CreditsD = models.CharField(max_length=12, default='',null=True)
    Dis_sys= models.CharField(max_length=500, default='',null=True) 

    GradeD1 = models.CharField(max_length=100,null=True)
    PointsD1 = models.CharField(max_length=30,null=True)
    CreditsD1 = models.CharField(max_length=12, default='',null=True)
    Design= models.CharField(max_length=500, default='',null=True) 

    GradeM = models.CharField(max_length=100,null=True)
    PointsM = models.CharField(max_length=30,null=True)
    CreditsM = models.CharField(max_length=12, default='',null=True)
    Mefa= models.CharField(max_length=500, default='',null=True) 

    GradeI = models.CharField(max_length=100,null=True)
    PointsI = models.CharField(max_length=30,null=True)
    CreditsI = models.CharField(max_length=12, default='',null=True)
    Info= models.CharField(max_length=500, default='',null=True) 
    
    

    Gradew1 = models.CharField(max_length=100,null=True)
    Pointsw1= models.CharField(max_length=30,null=True)
    Creditsw1 = models.CharField(max_length=12, default='',null=True)
    wlab= models.CharField(max_length=500, default='',null=True) 

    sgpa=models.CharField(max_length=5,null=True)

    Tot_cr=models.CharField(max_length=5,null=True)
     
    pass1=models.CharField(max_length=5,null=True)
    
    bclg=models.CharField(max_length=5,null=True)