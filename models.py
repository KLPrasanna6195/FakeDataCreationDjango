from django.db import models

# Create your models here.

class users(models.Model):
    id = models.IntegerField(primary_key=True);
    real_name = models.CharField(max_length=100);
    tz = models.CharField(max_length=100);
    activity_periods = models.TimeField(auto_now=True);
    start_time = models.DateTimeField();
    End_time = models.DateTimeField();