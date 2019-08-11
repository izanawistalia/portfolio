from django.shortcuts import render, get_object_or_404
from .models import blog

def allblog(request):
    blogs = blog.objects
    return render(request, 'blog/template/blog/allblog.html', { 'blogs':blogs } )


def blogdetail(request, blog_id):
    bdetail=get_object_or_404(blog, pk=blog_id)
    return render(request, 'blog/template/blog/detail.html', { 'blog':bdetail } )
