from django.db import models


class Professeur(models.Model):
    
    profId = models.AutoField(primary_key=True)
    experience = models.IntegerField(null=False, blank=False)
    orgId = models.IntegerField()
    fonction = models.CharField(null=False, blank=False, max_length=255)
    nomme = models.CharField(null=False, blank=False,max_length=5)
    tempprio = models.CharField(null=False, blank=False,max_length=5)
    tempor = models.CharField(null=False, blank=False,max_length=5)
    CAD =models.CharField(null=False, blank=False,max_length=3)
    CADFrom = models.DateField()
    CADTo = models.DateField()
    
    class Meta():
        db_table = "professeurs"

    

    