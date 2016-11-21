from django.contrib import admin
from .models import Contestant, Judge, Contest, Competence, Project, Mark

admin.site.register((Contestant, Judge, Contest, Competence, Project, Mark))
