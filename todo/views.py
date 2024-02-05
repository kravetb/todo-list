from django.views import generic

from todo.models import Tag, Task


class HomePageView(generic.ListView):
    model = Task
    template_name = "todo/index.html"


class TagListView(generic.ListView):
    model = Tag
