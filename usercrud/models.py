from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    doc_type = models.TextField(max_length=6)
    doc_num = models.IntegerField(primary_key=True)
    
    first_name = models.TextField(max_length=30)
    second_name = models.TextField(max_length=30)
    last_name = models.TextField(max_length=60)
    name_origin = models.TextField()
    
    birth_date = models.DateField()
    
    gender = models.TextField(max_length=50)
    cel_num = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.email
    
class Log(models.Model):
    ACTION_CHOICES = [
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
    ]
    action = models.CharField(max_length=6, choices=ACTION_CHOICES)
    user_doc = models.IntegerField()
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, to_field='doc_num')
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.action} - {self.user_doc} at {self.timestamp}"
    
    class Meta:
        indexes = [
            models.Index(fields=['user_doc']),
        ]

    