from rest_framework import viewsets, permissions
# from app.models import Contest, Competence, CompetenceType, Project, Mark, Judge, Contestant, User
# from .serializers import ContestSerializer, CompetenceSerializer, CompetenceTypeSerializer, ProjectSerializer, \
#     MarkSerializer, JudgeSerializer, ContestantSerializer, UserSerializer, ContestDepthSerializer
from app.models import Contest, Competence, CompetenceType, Project, Mark, Judge, User
from .serializers import ContestShortSerializer, CompetenceSerializer, CompetenceTypeSerializer, ProjectSerializer, \
    MarkSerializer, JudgeSerializer, UserSerializer, ContestDepthSerializer


class MarkPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and Judge.objects.filter(user=request.user)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user == obj.judge.user


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_fields = ('judges__contest', 'projects', 'projects__contest')


class JudgeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JudgeSerializer
    queryset = Judge.objects.all()
    filter_fields = '__all__'


# class ContestantViewSet(viewsets.ReadOnlyModelViewSet):
#     serializer_class = ContestantSerializer
#     queryset = Contestant.objects.all()
#     filter_fields = '__all__'


class ContestViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContestShortSerializer
    queryset = Contest.objects.all()
    filter_fields = ('judges__user', 'projects__contestants')


class CompetenceTypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompetenceTypeSerializer
    queryset = CompetenceType.objects.all()
    filter_fields = ('competences__contest',)


class CompetenceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompetenceSerializer
    queryset = Competence.objects.all()
    filter_fields = ('competence_type', 'contest')


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    filter_fields = ('contest', 'contest__judges__user', 'contestants')


class MarkViewSet(viewsets.ModelViewSet):
    serializer_class = MarkSerializer
    queryset = Mark.objects.all()
    permission_classes = (MarkPermissions,)
    filter_fields = ('judge__user', 'project', 'competence__competence_type')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ContestDepthViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContestDepthSerializer
    queryset = Contest.objects.all()
    filter_fields = ('judges__user', 'projects__contestants')
