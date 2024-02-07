from django.urls import path

from todo.views import HomePageView, TagListView, CompleteTaskView, UndoTaskView, TaskCreateView, TaskUpdateView, \
    TaskDeleteView, TagCreateView, TagUpdateView, TagDeleteView

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path('complete_task/<int:pk>/', CompleteTaskView.as_view(), name='complete_task'),
    path('undo_task/<int:pk>/', UndoTaskView.as_view(), name='undo_task'),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo"
