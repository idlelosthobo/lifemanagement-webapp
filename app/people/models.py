from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.timezone import now

from app.group.models import Group
from app.event.models import Event

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
    event = GenericRelation(Event, related_name='events', related_query_name='event')

    first_name = models.CharField(max_length=64, default='')
    middle_name = models.CharField(max_length=64, default='', blank=True)
    last_name = models.CharField(max_length=64, default='', blank=True)
    is_in_personal_life = models.BooleanField(default=False)
    is_in_work_life = models.BooleanField(default=False)
    relationship = models.CharField(max_length=4, choices=PEOPLE_RELATIONSHIP_CHOICES, default='frie')


