from django.db import models

# Create your models here.
class employesviws(models.Model):
    name=models.CharField(max_length=20)
    empid=models.IntegerField()
    email=models.EmailField( max_length=254)
    m_number=models.IntegerField()
    # password=models.CharField(max_length=50)


    def __str__(self):
        return self.name
    
class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)