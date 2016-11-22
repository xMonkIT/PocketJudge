from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from app.models import Contest, Competence, Project, Mark
from .serializers import ContestSerializer, CompetenceSerializer, ProjectSerializer, MarkSerializer


class ContestViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContestSerializer

    def get_queryset(self):
        return Contest.objects.all()\
            if self.request.user.is_superuser\
            else Contest.objects.filter(judges__user=self.request.user)


class CompetenceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompetenceSerializer
    filter_fields = ('contest_id',)

    def get_queryset(self):
        return Competence.objects.all()\
            if self.request.user.is_superuser\
            else Competence.objects.filter(contest__judges__user=self.request.user)


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    filter_fields = ('contest_id',)

    def get_queryset(self):
        return Project.objects.all()\
            if self.request.user.is_superuser\
            else Project.objects.filter(contest__judges__user=self.request.user)


class MarkViewSet(viewsets.ModelViewSet):
    serializer_class = MarkSerializer

    def get_queryset(self):
        return Mark.objects.all()\
            if self.request.user.is_superuser\
            else Mark.objects.filter(judge__user=self.request.user)
