# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    queryset_list = Post.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset_list, 2)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'title': 'List',
        'posts': queryset
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    instance = get_object_or_404(Post,pk=pk)
    context = {
        'title': 'Detail',
        'post': instance
    }
    return render(request, 'blog/post_detail.html', context)

def post_new(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        messages.success(request, "Successfully created")
        return redirect('posts:post_detail', pk=post.pk)
    else:
        form = PostForm()
        messages.error(request, "Not Successfully created")
    context = {
        'form': form
    }
    return render(request, 'blog/post_edit.html', context)

def post_edit(request, pk=None):
    instance = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            messages.success(request, "Updated")
            return redirect('posts:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=instance)

    context ={
        'form': form,
        'title': instance.title,
        'post': instance
    }
    messages.error(request, "Not Successfully updated")
    return render(request, 'blog/post_edit.html', context)

def post_delete(request, pk):
    instance = get_object_or_404(Post, pk=pk)
    instance.delete()
    messages.success(request, "Succesfully deleted")
    return redirect('posts:post_list')