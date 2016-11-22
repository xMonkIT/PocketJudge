from app.models import Contest, Competence, Project, Mark, Judge, Contestant, User
from rest_framework import serializers, permissions


class UserSerializer(serializers.ModelSerializer):
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


class ProjectOnlyUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('url',)


class ContestSerializer(serializers.HyperlinkedModelSerializer):
    projects = ProjectOnlyUrlSerializer(many=True)

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
        fields = '__all__'
        extra_kwargs = {'judge': {'read_only': True}}


class CompetenceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = ('id', 'name', 'url')


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'url')


class ContestDepthSerializer(serializers.ModelSerializer):
    competences = CompetenceModelSerializer(many=True)
    projects = ProjectModelSerializer(many=True)

    class Meta:
        model = Contest
        exclude = ('parent_contest', 'judges')
