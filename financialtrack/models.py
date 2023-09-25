from django.db import models

from django.contrib.auth.models import User

# Create your models here.
from group.models import Group

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tags_created')
    def __str__(self):
        return self.name
    
class FinancialRecord(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, related_name='records')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    debit = models.DecimalField(max_digits=16, decimal_places=6)
    credit = models.DecimalField(max_digits=16, decimal_places=6)
    currency = models.FloatField(default=1.00)
    balance = models.DecimalField(max_digits=16, decimal_places=6, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

