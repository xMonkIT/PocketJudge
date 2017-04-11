from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from app.forms import ProjectCompetencesForm
from .models import Contest, Project, Judge, Mark


class HomeView(ListView):
    model = Contest
    context_object_name = 'contests'
    template_name = 'app/home.html'
    queryset = Contest.objects.filter(parent_contest=None)


class ContestListView(ListView):
    model = Contest

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Contest.objects.filter(judges__user=self.request.user)
        return None


class ContestDetailView(DetailView):
    model = Contest


def project_detail_view(request, pk):
    project = Project.objects.get(pk=pk)
    judge = Judge.objects.filter(user=request.user, contest=project.contest).first()

    if request.POST:
        competences = project.contest.competences.all()

        for competence in competences:
            score = request.POST[str(competence.pk)]
            marks = Mark.objects.filter(project=project, judge=judge, competence=competence)

            if marks.exists():
                mark = marks.first()
                mark.score = score
                mark.save()
            else:
                Mark.objects.create(project=project, judge=judge, competence=competence, score=score)

        return redirect('app:my_contest_detail', pk=project.contest.pk)

    form = ProjectCompetencesForm(project, judge)
    return render(request, 'app/project_detail.html', context={
        'project': project,
        'form': form
    })
