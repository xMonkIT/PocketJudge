from rest_framework import viewsets, permissions
from app.models import Contest, Competence, Project, Mark, Judge, Contestant, User
from .serializers import ContestSerializer, CompetenceSerializer, ProjectSerializer, MarkSerializer, JudgeSerializer, \
    ContestantSerializer, UserSerializer, ContestDepthSerializer


class MarkPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.judge

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.judge == obj.judge


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


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class MarkViewSet(viewsets.ModelViewSet):
    serializer_class = MarkSerializer
    queryset = Mark.objects.all()
    permission_classes = (MarkPermissions,)


class ContestDepthViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContestDepthSerializer
    queryset = Contest.objects.all()
    filter_fields = ('judges',)
