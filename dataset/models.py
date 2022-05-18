from django.db import models

# Create your models here.
class dataset(models.Model):
    #video_path=models.TextField() #################
    video_blob=models.TextField(blank=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=1)
    age=models.IntegerField()
    gender=models.CharField(max_length=1)
    diagnosedWithADHD=models.BooleanField()
    responseTime =models.FloatField()
    correctTimingResponses=models.IntegerField()
    correctAttentionResponses=models.IntegerField()
    hyperactivityTarget=models.IntegerField()
    hyperactivityNonTarget=models.IntegerField()
    hyperactivityRandom=models.IntegerField()
    impulsiveResponses=models.IntegerField()
    omissionErrors=models.IntegerField()
    totalResponses=models.IntegerField()

