from django.db import models


class Position(models.TextChoices):
    PULLSTACK = "PullStack"
    BACKEND = "BackEme"
    FRONTEND = "FrontEnd"
    NONE = "None"


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


class JopPosting(TimeStampedModel):
    company = models.ForeignKey("Company", related_name="posting", on_delete=models.CASCADE)
    position = models.CharField(max_length=10, choices=Position.choices, default=Position.NONE)
    compensation = models.IntegerField()
    content = models.TextField()
    skill = models.CharField(max_length=100)
