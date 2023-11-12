from django.db import models
import os
import datetime



def filepath(request,filename):
    old_filename = filename
    timenow =datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" %(timenow,old_filename)
    return os.path.join('images/',filename)




# Create your models here.
class Student_Management(models.Model):
    Student_Adm = models.CharField(max_length=40,null=True)
    first_name = models.CharField(max_length=50,null=False)
    last_name = models.CharField(max_length=50,null=False)
    email = models.EmailField(max_length=50,null=False)
    field_of_study = models.CharField(max_length=100,null=False)
    year = models.TextField(max_length=4,null=False)
    image = models.ImageField(upload_to=filepath,null=True)

    def __str__(self) :
        return f"Student:{self.first_name} {self.last_name}"
    
