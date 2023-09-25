from django.contrib import admin

# Register your models here.
from .models import Tag, FinancialRecord

admin.site.register(Tag)
admin.site.register(FinancialRecord)