from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Comment,Post,LikePost

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

@login_required
def home(request):
    posts = Post.objects.filter(status=True).order_by('-pub_date')
    return render(request, 'post/post_all.html', {'posts':posts})

@login_required
def post(request, id):
    post = Post.objects.select_related().get(id=id)
    return render(request, 'post/post.html', {'post':post})

@login_required
def add_comment(request, id):
    return HttpResponse('add comment')

@login_required
def my_like(request,id):
    post = Post.objects.get(id=id)
    obj_type = ContentType.objects.get_for_model(post)
    like, is_created = LikePost.objects.get_or_create(
    content_type=obj_type, object_id=id, user=request.user)
    print('AAAAA',is_created)
    like.like_()
    like.save()
    print(like)

    return redirect('home')

@login_required
def dislike(reques,id):
    pass
