from django.urls import path

from todo.views import HomePageView, TagListView, complete_task, undo_task, TaskCreateView, TaskUpdateView, \
    TaskDeleteView

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path('complete_task/<int:pk>/', complete_task, name='complete_task'),
    path('undo_task/<int:pk>/', undo_task, name='undo_task'),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
]

app_name = "todo"
