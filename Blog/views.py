from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView, TemplateView, DeleteView
from Blog.models import Blog, Comment, Like
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from Blog.forms import CommentForm

# Create your views here.



class BlogList(ListView):
    context_object_name='blogs'
    model=Blog
    template_name='Blog/blog_list.html'

@login_required(login_url='/account/login/')
def blog_details(request, pk):
    blog=Blog.objects.get(pk=pk)
    comment_form=CommentForm()
    already_liked=Like.objects.filter(blog=blog,user=request.user)
    if already_liked:
        liked=True
    else:
        liked=False
    if request.method=='POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.user=request.user
            comment.blog=blog
            comment.save()
            return HttpResponseRedirect(reverse('Blog:blog_details', kwargs={'pk':pk}))

    return render(request, 'Blog/blog_details.html', context={'blog':blog, 'comment_form':comment_form, 'liked':liked})

@login_required(login_url='/account/login/')
def liked(request,pk):
    blog=Blog.objects.get(pk=pk)
    user=request.user
    already_liked=Like.objects.filter(blog=blog,user=user)
    if not already_liked:
        liked_post=Like(blog=blog,user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('Blog:blog_details', kwargs={'pk':pk}))

@login_required(login_url='/account/login/')
def unliked(request,pk):
    blog=Blog.objects.get(pk=pk)
    user=request.user
    already_liked=Like.objects.filter(blog=blog,user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('Blog:blog_details', kwargs={'pk':pk}))
