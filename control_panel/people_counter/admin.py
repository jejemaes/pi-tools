from django.contrib import admin
from .models import Counter, CounterItem

admin.site.register(Counter)
admin.site.register(CounterItem)
