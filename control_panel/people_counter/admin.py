from django.contrib import admin
from .models import Counter, CounterItem


class CounterAdmin(admin.ModelAdmin):
    list_display = ('date', 'name',)
    date_hierarchy = 'date'
    ordering = ('-date',)
    search_fields = ('name', 'date')


class CounterItemsAdmin(admin.ModelAdmin):
    list_display = ('date', 'count', 'counter')
    list_filter = ('date', 'counter',)
    date_hierarchy = 'date'
    ordering = ('-date',)


admin.site.register(Counter, CounterAdmin)
admin.site.register(CounterItem, CounterItemsAdmin)
