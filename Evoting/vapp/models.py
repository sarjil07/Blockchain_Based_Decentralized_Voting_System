from django.db import models

# Create your models here.
class Candidate(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=122)
    constituency=models.CharField(max_length=122)
    party=models.CharField(max_length=122)
    vcount=models.IntegerField()

    def __str__(self):
        return self.cname

class Voter(models.Model):
    aid=models.IntegerField()
    vname=models.CharField(max_length=122)
    city=models.CharField(max_length=122)
   
    def __str__(self):
        return self.vname
    
