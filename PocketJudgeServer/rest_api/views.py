from rest_framework import viewsets
from app.models import Contest, Competence, Project, Mark
from .serializers import ContestSerializer, CompetenceSerializer, ProjectSerializer, MarkSerializer


class ContestViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContestSerializer
    queryset = Contest.objects.all()
    filter_fields = ('judge_id',)


class CompetenceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompetenceSerializer
    queryset = Competence.objects.all()
    filter_fields = ('contest_id',)


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    filter_fields = ('contest_id',)


class MarkViewSet(viewsets.ModelViewSet):
    serializer_class = MarkSerializer
    queryset = Mark.objects.all()
    filter_fields = ('project_id', 'competence_id', 'judge_id')
