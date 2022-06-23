
from django.shortcuts import render, redirect, get_object_or_404
from .models import Club, Comment
# Create your views here.

def home(request):
    #sns 글들을 모조리 띄우는 코드
    #posts = Blog.objects.all()
    clubs = Club.objects.all()
    return render(request, 'index.html')

def detail(request, club_id):
    #blog_id 번째 블로그 글을 db에서 갖고와서 detail.html로 띄워주는 코드
    club_detail = get_object_or_404(Club, pk=club_id)

    #comment
    #comment_form = CommentModelForm()
    #return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form})
    return render(request, 'detail.html', {'club_detail':club_detail})

def new(request):
    if request.method == 'GET':
        return render(request, 'new.html')
    return redirect('home')

def create(request):

    if request.method == 'POST':
        club = Club()
        club.name = request.POST['name']
        club.num_clubmember = request.POST['num_clubmember']
        club.photo = request.FILES.get('photo')
        club.save()

    return redirect('home')