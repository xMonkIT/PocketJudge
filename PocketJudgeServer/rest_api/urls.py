from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'contests', views.ContestViewSet, base_name='contest')
router.register(r'competences', views.CompetenceViewSet, base_name='competence')
router.register(r'projects', views.ProjectViewSet, base_name='project')
router.register(r'marks', views.MarkViewSet, base_name='mark')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]