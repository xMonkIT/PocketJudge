from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'contests', views.ContestViewSet)
router.register(r'competences', views.CompetenceViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'marks', views.MarkViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]