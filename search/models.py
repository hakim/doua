from django.db import models

# Create your models here.
class Drug(models.Model):
    business_name = models.CharField(max_length=100)
    chemical_name = models.CharField(max_length=100)
    description   = models.TextField()
    
    def __unicode__(self):
        return '%s %s ' % (self.business_name,self.chemical_name)
