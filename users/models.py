from django.db import models


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100, verbose_name='email address')
    user_name = models.CharField(max_length=50, verbose_name='chosen user_name')
    car_name = models.ManyToManyField('Car', verbose_name='the user\'s cars')


STATUS_CHOICE = (
    ('r', 'Reviewed'),
    ('e', 'Error'),
    ('n', 'Not reviewed'),
    ('a', 'Accepted')
)


class Website(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=60, unique=True)
    release = models.DateField()
    rating = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICE, max_length=1)


class Car(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

