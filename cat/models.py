from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    time = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
    

class Term(models.Model):
    name = models.CharField(max_length=255)
    term_start_dt = models.DateField()
    term_end_dt = models.DateField()
    cat_yr = models.IntegerField()

    def __unicode__(self):
        return self.name
