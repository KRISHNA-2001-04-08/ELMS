from django.db import models
from django.contrib.auth.models import User


class Leave(models.Model):
    STATUS_CHOICES = [
('Pending', 'Pending'),
('Approved', 'Approved'),
('Rejected', 'Rejected')
]


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')


def __str__(self):
  return self.user.username