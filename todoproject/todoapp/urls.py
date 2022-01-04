
from django.urls import path
from . import views
app_name = 'todoapp'

urlpatterns = [
    path('', views.index,name='index'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:task_id>/',views.update,name='update'),
    path('cbv/',views.TaskListView.as_view(),name='cbv'),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete'),
]
