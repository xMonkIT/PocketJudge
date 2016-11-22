from app.models import Contest, Competence, Project, Mark
from rest_framework import serializers


class ContestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contest
        fields = ('url', 'id', 'name')


class CompetenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competence
        fields = ('url', 'id', 'name', 'max_mark')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('url', 'id', 'name', 'description')


class MarkSerializer(serializers.HyperlinkedModelSerializer):
    competence = CompetenceSerializer()
    project = ProjectSerializer()

    class Meta:
        model = Mark
        exclude = ('judge', )
