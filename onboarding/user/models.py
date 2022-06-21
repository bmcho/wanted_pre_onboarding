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


class User(TimeStampedModel):

    username = models.CharField(max_length=20, null=False)
    email = models.EmailField(unique=True, error_messages={"unique": "이미 사용중인 이메일입니다."})
    position = models.CharField(max_length=10, choices=Position.choices, default=Position.NONE)
    # job_posting = models.ManyToManyField("JopPosting")


class ApplyPosting(TimeStampedModel):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    posting = models.ForeignKey("jopPosting.JopPosting", on_delete=models.CASCADE)
