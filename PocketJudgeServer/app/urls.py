from datetime import datetime

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views as app_views, forms as app_forms

urlpatterns = [
    url(r'^$', app_views.home, name='home'),
    url(r'^login/$',
        auth_views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app_forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$', auth_views.logout, {'next_page': '/', }, name='logout'),
    url(r'logout-then-login', auth_views.logout_then_login)
]
