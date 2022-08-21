from django.db import models


class SatelliteInfo(models.Model):
    def __str__(self):
        return self.Name

    Name=models.CharField(max_length=200,blank=True,null=True)
    OrbitType=models.CharField(max_length=200,blank=True,null=True)
    OrbitDay=models.FloatField(max_length=200,blank=True,null=True)
    OrbitalPeriod=models.FloatField(max_length=200,blank=True,null=True)
    altitude=models.FloatField(default=0)
    Payload1=models.CharField(max_length=200,blank=True,null=True)
    Payload2=models.CharField(max_length=200,blank=True,null=True)
    Payload3=models.CharField(max_length=200,blank=True,null=True)
    SwathFore=models.FloatField(default=0)
    SwathAft=models.FloatField(default=0)
    IGFOVFore=models.FloatField(default=0)
    IGFOVAft=models.FloatField(default=0)
    TiltFore=models.FloatField(default=0)
    TiltAft=models.FloatField(default=0)



class SatNameId(models.Model):
    Name = models.CharField(max_length=50)
    SatId = models.PositiveIntegerField()

    def __str__(self):
        return self.Name