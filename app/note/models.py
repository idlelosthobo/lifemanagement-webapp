from django.db import models
from app.core.mixins import SecurityMixin, HistoryMixin, StatisticMixin


class Note(SecurityMixin, HistoryMixin, StatisticMixin):
    title = models.CharField(max_length=128, default='')
    information = models.TextField(default='')

    def short_title(self):
        short_length = 12
        if len(self.title) > short_length:
            return '%s...' % self.title[:short_length]
        else:
            return self.title

    class Meta:
        ordering = ('-id',)