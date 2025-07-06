from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

#@login_required
def admin_panel(request):
    posts = Post.objects.all().order_by('created_at')
    return render(request, 'posts/admin_panel.html', {'posts': posts})

#@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = PostForm()
    return render(request, 'posts/new_post.html', {'form':form})

#@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('admin_panel')

def post_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request,'posts/post_list.html',{'posts':posts})

