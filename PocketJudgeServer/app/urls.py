from datetime import datetime

from django.conf.urls import url
from django.contrib.auth.views import login, logout, logout_then_login
from .views import ContestListView, ContestDetailView, HomeView, project_detail_view
from .forms import BootstrapAuthenticationForm

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login/$',
        login,
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout/$', logout, {'next_page': '/', }, name='logout'),
    url(r'logout-then-login/$', logout_then_login),
    url(r'my-contests/$', ContestListView.as_view(), name='my_contests'),
    url(r'my-contests/(?P<pk>\d+)/$', ContestDetailView.as_view(), name='my_contest_detail'),
    url(r'my-projects/(?P<pk>\d+)/$', project_detail_view, name='my_project_detail')
]
