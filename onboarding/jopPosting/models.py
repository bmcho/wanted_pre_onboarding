from django.db import models

# Create your models here.
class Position(models.TextChoices):
    PULLSTACK = "PullStack"
    BACKEND = "BackEme"
    FRONTEND = "FrontEnd"
    NONE = "None"


class TimeStampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class JopPosting(TimeStampedModel):
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE)
    position = models.CharField(max_length=10, choices=Position.choices, default=Position.NONE)
    compensation = models.IntegerField()
    content = models.TextField()
    skill = models.CharField(max_length=100)
