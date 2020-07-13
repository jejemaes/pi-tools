
from django.db import models
from django.utils import timezone


class Counter(models.Model):
    date = models.DateTimeField(default=timezone.now, verbose_name="Date", null=False)
    name = models.CharField(max_length=100, blank=False)

    class Meta:
        verbose_name = "Counter"
        ordering = ['-date']

    def __str__(self):
        return self.name


class CounterItem(models.Model):
    date = models.DateTimeField(default=timezone.now, verbose_name="Date", null=False)
    count = models.IntegerField(default=0)
    counter = models.ForeignKey('Counter', null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Counter Item"
        ordering = ['-date']

    def __str__(self):
        return f"{self.count} people at {self.date}"
