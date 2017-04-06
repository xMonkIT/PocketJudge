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


class ProjectOnlyUrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('url',)


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
        fields = ('id', 'name', 'url')


class CompetenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competence
        fields = '__all__'


class CompetenceModelSerializer(serializers.ModelSerializer):
    competence_type = CompetenceTypeModelSerializer

    class Meta:
        model = Competence
        fields = ('id_competence', 'competence_type', 'max_score', 'url')


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


class ContestSerializer(serializers.HyperlinkedModelSerializer):
    projects = ProjectOnlyUrlSerializer(many=True)

    class Meta:
        model = Contest
        exclude = ('mark_availability_type',)


class ContestDepthSerializer(serializers.ModelSerializer):
    competences = CompetenceModelSerializer(many=True)
    projects = ProjectModelSerializer(many=True)

    class Meta:
        model = Contest
        exclude = ('parent_contest', 'mark_availability_type')
