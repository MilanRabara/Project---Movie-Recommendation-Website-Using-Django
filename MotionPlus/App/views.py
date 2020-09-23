from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from .models import Movie, Myrating
from django.contrib import messages


def home_page(request):
    return render(request, 'home.html')


def movielist(request):
    movies = Movie.objects.all()
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(Q(title__icontains=query)).distinct()
        return render(request, 'MoviesList.html', {'movies': movies})
    return render(request, 'MoviesList.html', {'movies': movies})


def login(request):
    return render(request, 'registration/login.html')


def page(request):
    return render(request, 'home.html')


def sign_up(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username1', False)
            email = request.POST.get('email1', False)
            password = request.POST.get('password1', False)
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            return redirect('login')
        except:
            return render(request, 'registration/login.html')
    return render(request, 'registration/login.html')


def detail(request, movie_id):
    if not request.user.is_authenticated:
        return redirect("login")
    if not request.user.is_active:
        raise Http404
    movies = get_object_or_404(Movie, id=movie_id)
    # for rating
    if request.method == "POST":
        rate = request.POST['rating']
        ratingObject = Myrating()
        ratingObject.user = request.user
        ratingObject.movie = movies
        ratingObject.rating = rate
        ratingObject.save()
        messages.success(request, "Your Rating is submited ")
        return redirect('movies')
    return render(request, 'details.html', {'movies': movies})
