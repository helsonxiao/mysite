from django.shortcuts import render
from django.utils import timezone
from .models import Post  # The dot before models means current directory or current application.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    # add some things for the template to use
    return render(request, 'blog/post_list.html', {'posts': posts})
    