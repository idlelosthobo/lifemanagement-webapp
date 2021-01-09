from django.db import models
from django.utils.timezone import now
from django.contrib.contenttypes.fields import GenericRelation
from app.core.models import Security, Statistic


class SecurityMixin(models.Model):
    security = GenericRelation(Security, related_name='securities', related_query_name='security')

    def update_security(self, user):
        try:
            security = Security.objects.get(content_type__model=self, object_id=self.pk, user=user)
        except Statistic.DoesNotExist:
            security = None
        if security:
            security.user = user
            security.save()
        else:
            self.security.create(view_count=1, user=user)

    class Meta:
        abstract = True


class HistoryMixin(models.Model):
    is_archived = models.BooleanField(default=False, editable=False)
    is_to_be_deleted = models.BooleanField(default=False, editable=False)
    deletion_date = models.DateField(auto_now_add=True, editable=False)

    def set_to_be_deleted(self):
        self.is_to_be_deleted = True
        self.save()

    def un_set_to_be_deleted(self):
        self.is_to_be_deleted = False
        self.save()

    def set_archived(self):
        self.is_archived = True
        self.save()

    def un_set_archived(self):
        self.is_archived = False
        self.save()

    class Meta:
        abstract = True


class StatisticMixin(models.Model):
    date_entered = models.DateTimeField(auto_now_add=True, editable=False)
    date_updated = models.DateTimeField(auto_now=True, editable=False)
    statistic = GenericRelation(Statistic, related_name='statistics', related_query_name='statistic', editable=False)

    def update_statistic(self, user):
        try:
            statistic = Statistic.objects.get(content_type__model=self, object_id=self.pk, user=user)
        except Statistic.DoesNotExist:
            statistic = None
        if statistic:
            statistic.view_count += 1
            statistic.save()
        else:
            self.statistic.create(view_count=1, user=user)

    class Meta:
        abstract = True