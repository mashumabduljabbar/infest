from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import (TemplateView,ListView,DetailView,
                                    CreateView,DetailView,UpdateView,
                                    DeleteView,)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from porfolio.forms import PostForm,CommentForm
from porfolio.models import Post,Comment

# Create your views here.


####### Post related class and def ##################

class AboutView(TemplateView):
    template_name = 'porfolio/about.html'

class HomeView(TemplateView):
    template_name = 'porfolio/base.html'

class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') #minus (-) infront of published_date order in decending

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    template_name = 'post/post_form.html'
    redirect_field_name = 'post/post_detail.html'

    form_class =PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    template_name = 'post/post_form.html'
    redirect_field_name = 'post/post_detail.html'

    form_class =PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    template_name = 'post/post_draft_list.html'
    redirect_field_name = 'post/post_draft_list.html'

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-create_date')

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

####### Comment related class and def ##################


def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'post/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
