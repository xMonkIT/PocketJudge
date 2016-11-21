from django.template.loader_tags import register


@register.filter
def projects_sums(projects):
    return [(project.name, sum([x.mark for x in project.mark_set.all()])) for project in projects]