from django.db import models


class SecurityMixin(models.Model):
    pass

    class Meta:
        abstract = True


class ArchiveMixin(models.Model):
    pass

    class Meta:
        abstract = True


