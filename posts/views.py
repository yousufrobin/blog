from django.shortcuts import render
from posts.models import Posts


# Create your views here.


def index(request):
    posts = Posts.objects.all()
    return render(request, "index.html", {"context": posts})


def postviewer(request, post_id):
    post = Posts.objects.get(id=post_id)
    return render(request, "postviewer.html", {"context": post})
