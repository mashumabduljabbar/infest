from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,ListView,DetailView,
                                    CreateView,DetailView,UpdateView,
                                    DeleteView,)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm
from projects.models import Project

# Create your views here.


####### Post related class and def ##################

class ProjectsListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    def get_queryset(self):
        return Project.objects.order_by('-priority') #minus (-) infront of published_date order in decending

class ProjectsDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
