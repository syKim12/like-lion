from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm

# Create your views here.
def home(request):
    #sns 글들을 모조리 띄우는 코드
    #posts = Blog.objects.all()
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts':posts})

#블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

#블로그 글을 저장해주는 함수
def create(request):
    if (request.method == 'POST'):
        post = Post()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.photo = request.POST['photo']
        post.date = timezone.now()
        post.save()

    return redirect('home')

def formcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        form = PostForm()
        return render(request, 'formcreate.html', {'form':form})

def detail(request, blog_id):
    #blog_id 번째 블로그 글을 db에서 갖고와서 detail.html로 띄워주는 코드
    blog_detail = get_object_or_404(Post, pk=blog_id)

    #comment
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail':blog_detail, 'comment_form':comment_form})

def create_comment(request, post_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()

    return redirect('detail', post_id)