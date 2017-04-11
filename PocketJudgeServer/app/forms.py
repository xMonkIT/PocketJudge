"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from app.models import Mark


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses bootstrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Пароль'}))


class ProjectCompetencesForm(forms.Form):
    def __init__(self, project, judge, *args, **kwargs):
        super().__init__(*args, **kwargs)

        competences = project.contest.competences.all()
        for competence in competences:
            self.fields[str(competence.pk)] = forms.IntegerField(
                min_value=0,
                max_value=competence.max_score,
                label=competence.competence_type.name,
                widget=forms.NumberInput({
                    'class': 'form-control'
                })
            )
            marks = Mark.objects.filter(project=project, judge=judge, competence=competence)
            if marks.exists():
                mark = marks.first()
                self.fields[str(competence.pk)].initial = mark.score
            if kwargs.get(str(competence.pk), None):
                self.fields[str(competence.pk)].initial = int(kwargs.get(str(competence.pk)))
