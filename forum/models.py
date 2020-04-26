from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#TODO change to enum
rate_choices = (
    ("1", "Salary"),
    ("2", "Hourly"),
    ("3", "Monthy"),
    ("4", "Weekly"),
    ("5", "Biweekly"),
)

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.CharField(max_length=1, choices=rate_choices, default="1")
    income = models.PositiveIntegerField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __int__(self):
        return self.income

    def get_absolute_url(self):
        return reverse('income-detail', kwargs={'pk':self.pk})