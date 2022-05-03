from django.db import models


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100)
    user_name = models.CharField(max_length=50)


STATUS_CHOICE = (
    ('r', 'Reviewed'),
    ('e', 'Error'),
    ('n', 'Not reviewed'),
    ('a', 'Accepted')
)


class Website(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=60)
    release = models.DateField()
    rating = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICE, max_length=1)


