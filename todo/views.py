from django.views import generic

from todo.models import Tag


class HomePageView(generic.base.TemplateView):
    template_name = "todo/index.html"


class TagListView(generic.ListView):
    model = Tag
