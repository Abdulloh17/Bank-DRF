from django.contrib import admin
from .models import User, HistoryTransfer

# Register your models here.
admin.site.register(User)
admin.site.register(HistoryTransfer)
