from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_POST

from todo.models import Tag, Task


class HomePageView(generic.ListView):
    model = Task
    template_name = "todo/index.html"


class TagListView(generic.ListView):
    model = Tag


@require_POST
def complete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.implementation = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:index"))


@require_POST
def undo_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.implementation = False
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:index"))


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
