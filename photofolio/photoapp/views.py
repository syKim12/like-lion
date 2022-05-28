from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentModelForm

# Create your views here.
def home(request):
    #sns 글들을 모조리 띄우는 코드
    #posts = Blog.objects.all()
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts':posts})

#블로그 글 작성 html을 보여주는 함수
def new(request):
    if request.method == 'GET':
        return render(request, 'new.html')


#블로그 글을 저장해주는 함수
def create(request):

    if request.method == 'POST':
        post = Post()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.photo = request.FILES.get('photo')
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

def detail(request, post_id):
    #blog_id 번째 블로그 글을 db에서 갖고와서 detail.html로 띄워주는 코드
    post_detail = get_object_or_404(Post, pk=post_id)

    #comment
    comment_form = CommentModelForm()
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

"""def modelformcreate(request):
    #입력을 받을 수 있는 html을 갖다주기
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            #저장
            form.save()
            return redirect('home')
    else:
        form = BlogModelForm()
    #render()의 세번째 인자로 views.py 내의 데이터를 dictionary 자료형으로 html 넘길 수 있음.
    return render(request, 'form_create.html', {'form':form})"""

def create_comment(request, post_id):
    filled_form = CommentModelForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()

    return redirect('detail', post_id)

