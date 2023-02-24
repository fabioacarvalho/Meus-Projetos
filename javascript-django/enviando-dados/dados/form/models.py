from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    sobrenome = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return "%s - %s - %d" % self.name, self.sobrenome, self.age