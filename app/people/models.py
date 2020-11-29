from django.db import models
from app.group.models import Group
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, editable=False)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, related_name='person', related_query_name='people', editable=False)

