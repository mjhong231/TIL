from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
# Create your views here.
def index(request):
    movies = Movie.objects.all()

    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie':movie,
    }

    return render(request, 'movies/detail.html', context)

def create(request):
    if request.method =='POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
        return redirect('movies:detail', movie.pk)
    
    else:
        form = MovieForm()
    
    context = {
        'form':form,
    }
    return render(request, 'movies/create.html', context)

def delete(request, pk):
    article = Movie.objects.get(pk=pk)
    article.delete()
    
    return redirect('movies:index')

def update(request, pk):
    movie = Movie.objects.get(pk = pk)
    if request.method == 'POST':
        # 기존 게시글의 데이터를 미리 채운다 
        form = MovieForm(request.POST, request.FILES, instance = movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    # 변경 버튼 누르기 전 또는 다른 버튼 눌렀을때
    else:
        form = MovieForm(instance = movie)

    context = {
        # 기존에 존재했던 title과 content
        'movie':movie,
        'form': form,
    }
    return render(request, 'movies/update.html', context)