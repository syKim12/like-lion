from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm

# Create your views here.
def home(request):
    #블로그 글들을 모조리 띄우는 코드
    #posts = Blog.objects.all()
    posts = Blog.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts':posts})

#블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

#블로그 글을 저장해주는 함수
def create(request):
    if (request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()

    return redirect('home')

#django form을 이용해서 입력값을 받는 함수
#GET 요청과 (=입력값을 받을 수 있는 html을 갖다 줘야함)
#POST 요청 (=입력한 내용을 데이터베이스에 저장. form에서 입력한 내용을 처리)
#둘다 처리가 가능한 함수
def formcreate(request):
    #입력을 받을 수 있는 html을 갖다주기
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            #저장
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        form = BlogForm()
    #render()의 세번째 인자로 views.py 내의 데이터를 dictionary 자료형으로 html 넘길 수 있음.
    return render(request, 'form_create.html', {'form':form})


def modelformcreate(request):
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
    return render(request, 'form_create.html', {'form':form})

def detail(request, blog_id):
    #blog_id 번째 블로그 글을 db에서 갖고와서 detail.html로 띄워주는 코드
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    #comment
    comment_form = CommentForm()
    return render(request, 'detail.html', {'blog_detail':blog_detail, 'comment_form':comment_form})

def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()

    return redirect('detail', blog_id)