from django.db import models


class SecurityMixin(models.Model):
    pass

    class Meta:
        abstract = True


class ArchiveMixin(models.Model):
    is_archived = models.BooleanField(default=False)

    def archive(self):
        self.is_archived = True

    def un_archive(self):
        self.is_archived = False

    class Meta:
        abstract = True


