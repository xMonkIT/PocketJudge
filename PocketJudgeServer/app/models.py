# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Competence(models.Model):
    id_competence = models.AutoField(db_column='IdCompetence', primary_key=True)
    max_score = models.IntegerField(db_column='MaxScore')
    competence_type = models.ForeignKey('CompetenceType', models.DO_NOTHING, db_column='IdCompetenceType', related_name='competences')
    contest = models.ForeignKey('Contest', models.DO_NOTHING, db_column='IdContest', related_name='competences')

    def __str__(self):
        return str(self.contest) + ": " + self.competence_type.name + " (" + str(self.max_score) + ")"

    class Meta:
        db_table = 'Competence'
        unique_together = (('competence_type', 'contest'),)


class CompetenceType(models.Model):
    id_competence_type = models.AutoField(db_column='IdCompetenceType', primary_key=True)
    name = models.CharField(db_column='Name', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'CompetenceType'


class Contest(models.Model):
    id_contest = models.AutoField(db_column='IdContest', primary_key=True)
    name = models.CharField(db_column='Name', max_length=255)
    description = models.CharField(db_column='Description', max_length=1024, blank=True, null=True)
    datetime_begin = models.DateTimeField(db_column='DatetimeBegin')
    datetime_end = models.DateTimeField(db_column='DatetimeEnd', blank=True, null=True)
    max_count_contestant_on_project = models.IntegerField(db_column='MaxCountContestantOnProject', blank=True, null=True)
    max_count_project_on_contestant = models.IntegerField(db_column='MaxCountProjectOnContestant', blank=True, null=True)
    contestant_judge = models.BooleanField(db_column='ContestantJudge')
    parent_contest = models.ForeignKey('self', models.DO_NOTHING, db_column='IdParentContest', blank=True, null=True, related_name='contests')
    mark_availability_type = models.ForeignKey('MarkAvailabilityType', models.DO_NOTHING, db_column='IdMarkAvailabilityType', related_name='contests')

    def __str__(self):
        return (str(self.parent_contest) + "/" if self.parent_contest else "") + self.name

    class Meta:
        db_table = 'Contest'

#
# class Contestant(models.Model):
#     id_contestant = models.AutoField(db_column='IdContestant', primary_key=True)
#     user = models.ForeignKey(User, models.DO_NOTHING, db_column='IdUser', related_name='contestants')
#     project = models.ForeignKey('Project', models.DO_NOTHING, db_column='IdProject', related_name='contestants')
#
#     def __str__(self):
#         return str(self.project) + ": " + str(self.user)
#
#     class Meta:
#         db_table = 'Contestant'
#         unique_together = (('user', 'project'),)


class Judge(models.Model):
    id_judge = models.AutoField(db_column='IdJudge', primary_key=True)
    datetime_session_end = models.DateTimeField(db_column='DatetimeSessionEnd', blank=True, null=True)
    contest = models.ForeignKey(Contest, models.DO_NOTHING, db_column='IdContest', related_name='judges')
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='IdUser', related_name='judges')

    def __str__(self):
        return str(self.contest) + ": " + str(self.user)

    class Meta:
        db_table = 'Judge'
        unique_together = (('contest', 'user'),)


class Mark(models.Model):
    id_mark = models.AutoField(db_column='IdMark', primary_key=True)
    competence = models.ForeignKey(Competence, models.DO_NOTHING, db_column='IdCompetence', related_name='marks')
    project = models.ForeignKey('Project', models.DO_NOTHING, db_column='IdProject', related_name='marks')
    judge = models.ForeignKey(Judge, models.DO_NOTHING, db_column='IdJudge', related_name='marks')
    score = models.IntegerField(db_column='Score')

    def __str__(self):
        return str(self.project) + " - " + str(self.judge) + " - " + str(self.competence) + ": " + str(self.score)

    class Meta:
        db_table = 'Mark'
        unique_together = (('competence', 'project', 'judge'),)


class MarkAvailabilityType(models.Model):
    id_mark_availability_type = models.AutoField(db_column='IdMarkAvailabilityType', primary_key=True)
    name = models.CharField(db_column='Name', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'MarkAvailabilityType'


class Project(models.Model):
    id_project = models.AutoField(db_column='IdProject', primary_key=True)
    name = models.CharField(db_column='Name', max_length=255)
    description = models.CharField(db_column='Description', max_length=1024, blank=True, null=True)
    contest = models.ForeignKey(Contest, models.DO_NOTHING, db_column='IdContest', related_name='projects')
    contestants = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Project'
