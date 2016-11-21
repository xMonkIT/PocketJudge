from django.contrib.auth.models import User
from django.db import models


class Contestant(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.__str__()


class Judge(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.__str__()


class Competence(models.Model):
    name = models.CharField(max_length=255)
    max_mark = models.IntegerField(default=10)

    def __str__(self):
        return self.name


class Contest(models.Model):
    name = models.CharField(max_length=255)
    parent_contest = models.ForeignKey('self', null=True, blank=True)
    judges = models.ManyToManyField(Judge, blank=True)
    competences = models.ManyToManyField(Competence, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1024, null=True, blank=True)
    contest = models.ForeignKey(Contest)
    contestants = models.ManyToManyField(Contestant)

    def __str__(self):
        return self.name + " - " + (self.description[:20] + "..." if len(self.description) > 20 else self.description)


class Mark(models.Model):
    mark = models.IntegerField()
    competence = models.ForeignKey(Competence)
    project = models.ForeignKey(Project)
    judge = models.ForeignKey(Judge)

    def __str__(self):
        return self.mark.__str__()

    class Meta:
        unique_together = ("competence", "project", "judge")
