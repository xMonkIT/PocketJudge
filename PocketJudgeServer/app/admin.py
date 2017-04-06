from django.contrib import admin
from .models import Judge, Contest, Competence, Project, Mark  # , Contestant

# admin.site.register((Contestant, Judge, Contest, Competence, Project, Mark))
admin.site.register((Judge, Contest, Competence, Project, Mark))
