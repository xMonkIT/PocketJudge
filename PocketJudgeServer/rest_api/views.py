from rest_framework import viewsets
from app.models import Contest, Competence, Project, Mark, Judge, Contestant, User
from .serializers import ContestSerializer, CompetenceSerializer, ProjectSerializer, MarkSerializer, JudgeSerializer, \
    ContestantSerializer, UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class JudgeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JudgeSerializer
    queryset = Judge.objects.all()


class ContestantViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContestantSerializer
    queryset = Contestant.objects.all()


class ContestViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContestSerializer
    queryset = Contest.objects.all()
    filter_fields = ('judges__user_id',)


class CompetenceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompetenceSerializer
    queryset = Competence.objects.all()
    filter_fields = ('contest',)


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    filter_fields = ('contest',)


class MarkViewSet(viewsets.ModelViewSet):
    serializer_class = MarkSerializer
    queryset = Mark.objects.all()
    filter_fields = ('project_id', 'competence_id', 'judge__user_id', 'project')
