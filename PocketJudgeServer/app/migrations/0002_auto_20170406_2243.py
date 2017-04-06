# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-06 19:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contestant',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='project',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='user',
        ),
        migrations.AddField(
            model_name='project',
            name='contestants',
            field=models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='competence',
            name='competence_type',
            field=models.ForeignKey(db_column='IdCompetenceType', on_delete=django.db.models.deletion.DO_NOTHING, related_name='competences', to='app.CompetenceType'),
        ),
        migrations.AlterField(
            model_name='competence',
            name='contest',
            field=models.ForeignKey(db_column='IdContest', on_delete=django.db.models.deletion.DO_NOTHING, related_name='competences', to='app.Contest'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='mark_availability_type',
            field=models.ForeignKey(db_column='IdMarkAvailabilityType', on_delete=django.db.models.deletion.DO_NOTHING, related_name='contests', to='app.MarkAvailabilityType'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='parent_contest',
            field=models.ForeignKey(blank=True, db_column='IdParentContest', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='contests', to='app.Contest'),
        ),
        migrations.AlterField(
            model_name='judge',
            name='contest',
            field=models.ForeignKey(db_column='IdContest', on_delete=django.db.models.deletion.DO_NOTHING, related_name='judges', to='app.Contest'),
        ),
        migrations.AlterField(
            model_name='judge',
            name='user',
            field=models.ForeignKey(db_column='IdUser', on_delete=django.db.models.deletion.DO_NOTHING, related_name='judges', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mark',
            name='competence',
            field=models.ForeignKey(db_column='IdCompetence', on_delete=django.db.models.deletion.DO_NOTHING, related_name='marks', to='app.Competence'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='judge',
            field=models.ForeignKey(db_column='IdJudge', on_delete=django.db.models.deletion.DO_NOTHING, related_name='marks', to='app.Judge'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='project',
            field=models.ForeignKey(db_column='IdProject', on_delete=django.db.models.deletion.DO_NOTHING, related_name='marks', to='app.Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='contest',
            field=models.ForeignKey(db_column='IdContest', on_delete=django.db.models.deletion.DO_NOTHING, related_name='projects', to='app.Contest'),
        ),
        migrations.DeleteModel(
            name='Contestant',
        ),
    ]
