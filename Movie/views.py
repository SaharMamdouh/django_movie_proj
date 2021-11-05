from django.shortcuts import render
from .models import Movie
from .forms import MovieForm
# Create your views here.
def movie(request):
    return render(request,'movie/movie.html')

def movies(request):
    data=request.POST
    media=request.FILES
    form = MovieForm(data,files=media)
    if request.method=="POST":
        print('request is post')
        if form.is_valid():
           print ('form is valid')
           form.save()
        else:
           print('invalid form')

    return render(request,'movie/movies.html',{'mov':Movie.objects.all(),'form':form})

def update(request,movie_id):
    updated_movie=Movie.objects.get(pk=movie_id)
    form = MovieForm(instance=updated_movie)
    if request.method == "POST":
        print('request is post')
        form = MovieForm(instance=updated_movie,data=request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            form=MovieForm()

    return render(request, 'movie/movies.html', {'mov': Movie.objects.all(),'form':form})

def delete(request,movie_id):
    deleted_movie = Movie.objects.get(pk=movie_id)
    form = MovieForm()
    if request.method == "GET":
        print('request is get')
        deleted_movie.delete()
    return render(request, 'movie/movies.html', {'mov': Movie.objects.all(),'form':form})

def view(request,movie_id):
    return render(request, 'movie/movie.html', {'mov': Movie.objects.get(pk=movie_id)})
