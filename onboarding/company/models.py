from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Company(TimeStampedModel):
    companyname = models.CharField(max_length=200, null=False)
    country = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
