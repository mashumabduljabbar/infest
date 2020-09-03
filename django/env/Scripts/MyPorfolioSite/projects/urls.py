from django.urls import path
from projects import views



urlpatterns = [
    path('',views.ProjectsListView.as_view(),name='project_list'),
    path('<int:pk>',views.ProjectsDetailView.as_view(),name='project_detail'),
]
