from django.db import models

class PublishedManager(models.Manager):
    def get_queryset(self):
        from .models import News#shunday qilinadi deyildi
        return super().get_queryset().filter(status=News.Status.Published)
