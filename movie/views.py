from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie
from django.db.models import Q
from .forms import RegistrationForm
from .forms import CommentForm
# Create your views here.


def index(request):
    Data = {"Movies": Movie.objects.all()}
    return render(request, "pages/home.html", Data)


def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        Data = Movie.objects.filter(Q(name__icontains=search))
        return render(request, "pages/search.html", {'Movies': Data, 'search': search})
    else:
        return render(request, "pages/home.html", {})


def getMovieById(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, "pages/movie.html", {'movie': movie, 'n': range(movie.rating), 'm': range(5-movie.rating)})


def watchMovie(request, id):
    movie = Movie.objects.get(id=id)
    data = Movie.objects.all().order_by("-rating").values()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, author=request.user, movie=movie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "pages/watchmovie.html", {'movie': movie, 'Movies': data, 'form': form})


def getType(request):
    if request.method == 'GET':
        type = request.GET.get('type')
        Data = Movie.objects.filter(category__name=type)
        return render(request, "pages/typemovie.html", {'Movies': Data, 'type': type})
    else:
        return render(request, "pages/home.html", {})


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})

def error(request, exception):
    return render(request, 'pages/error.html')

def error1(request):
    return render(request, 'pages/error.html')