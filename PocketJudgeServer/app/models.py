from django.contrib.auth.models import User
from django.db import models


class Contestant(models.Model):
    user = models.OneToOneField(User)


class Judge(models.Model):
    user = models.OneToOneField(User)


class Contest(models.Model):
    name = models.TextField(max_length=255)
    parent_contest = models.ForeignKey('self', null=True, blank=True)
    judges = models.ManyToManyField(Judge)


class Competence(models.Model):
    name = models.TextField(max_length=255)
    max_mark = models.IntegerField(default=10)
    contest = models.ForeignKey(Contest)


class Project(models.Model):
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=1024, null=True, blank=True)
    contestants = models.ManyToManyField(Contestant)


class Mark(models.Model):
    mark = models.IntegerField()
    competence = models.ForeignKey(Competence)
    project = models.ForeignKey(Project)
    judge = models.ForeignKey(Judge)

    class Meta:
        unique_together = ("competence", "project", "judge")
