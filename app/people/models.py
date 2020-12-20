from django.db import models
from app.group.models import Group
from django.contrib.auth.models import User
from django.utils.timezone import now

PEOPLE_RELATIONSHIP_CHOICES = (
    ('frie', 'Friend'),
    ('part', 'Partner'),
    ('chil', 'Child'),
    ('pare', 'Parent'),
    ('acqu', 'Acquaintance'),
    ('ment', 'Mentor'),
)


class People(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='person', related_query_name='people', editable=False)

    first_name = models.CharField(max_length=64, default='')
    middle_name = models.CharField(max_length=64, default='', blank=True)
    last_name = models.CharField(max_length=64, default='', blank=True)
    is_in_personal_life = models.BooleanField(default=False)
    is_in_work_life = models.BooleanField(default=False)
    relationship = models.CharField(max_length=4, choices=PEOPLE_RELATIONSHIP_CHOICES, default='frie')


class PeopleDates(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE, related_name='dates', related_query_name='date')
    name = models.CharField(max_length=32)
    start = models.DateTimeField(default=now)
    finish = models.DateTimeField(default=now)