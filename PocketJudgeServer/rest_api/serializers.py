from app.models import Contest, Competence, Project, Mark, Judge, Contestant, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class JudgeSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Judge
        fields = '__all__'


class ContestantSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Contestant
        fields = '__all__'


class ContestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contest
        fields = '__all__'


class CompetenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competence
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class MarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mark
        exclude = '__all__'
