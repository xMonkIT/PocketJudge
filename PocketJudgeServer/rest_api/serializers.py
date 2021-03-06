from django.db import DatabaseError
from rest_framework.exceptions import ValidationError

from app.models import Contest, Competence, CompetenceType, Project, Mark, Judge, User
# from app.models import Contest, Competence, CompetenceType, Project, Mark, Judge, Contestant, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class JudgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Judge
        fields = '__all__'


# class ContestantSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Contestant
#         fields = '__all__'


class ProjectShortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('url', 'name')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id_project', 'name', 'description', 'url')


class CompetenceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompetenceType
        fields = '__all__'


class CompetenceTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetenceType
        fields = ('name',)


class CompetenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competence
        fields = '__all__'


class CompetenceModelSerializer(serializers.ModelSerializer):
    competence_type = CompetenceTypeModelSerializer

    class Meta:
        model = Competence
        fields = ('id_competence', 'url', 'competence_type', 'max_score')


class MarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'
        extra_kwargs = {'judge': {'read_only': True}}

    def create(self, validated_data):
        user = validated_data.pop('user')
        contest = Contest.objects.filter(projects=validated_data.get('project'))[0]
        judges = Judge.objects.filter(user=user, contest=contest)
        validated_data['judge'] = judges[0] if judges else None

        try:
            mark = Mark.objects.create(**validated_data)
        except DatabaseError as err:
            raise ValidationError(err.__cause__.__context__.excepinfo[2])

        return mark


class ContestShortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contest
        fields = ('url', 'name')


class ContestDepthSerializer(serializers.ModelSerializer):
    competences = CompetenceModelSerializer(many=True)
    projects = ProjectShortSerializer(many=True)

    class Meta:
        model = Contest
        fields = ('name', 'description', 'datetime_begin', 'datetime_end', 'competences', 'projects')
