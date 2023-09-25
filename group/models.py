from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=100)
    weight = models.IntegerField(default=1)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='groups_created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.group_name