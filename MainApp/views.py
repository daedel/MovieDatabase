from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView

from MainApp.models import Movie
from MainApp.services import get_movie_info_by_title, get_movie_info_by_id


class MainView(TemplateView):
    PAGINATION_ITEMS_PER_PAGE = 5
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        title = self.request.GET.get("title")

        if not title:
            return {}

        page = self.request.GET.get("page")
        per_page = self.request.GET.get("per_page", self.PAGINATION_ITEMS_PER_PAGE)

        objects = get_movie_info_by_title(title)
        if not objects:
            return {}
        
        paginator = Paginator(objects, per_page)

        try:
            movie_info = paginator.page(page)
        except PageNotAnInteger:
            movie_info = paginator.page(1)
        except EmptyPage:
            movie_info = paginator.page(paginator.num_pages)

        context = {
            "movie_info": movie_info,
        }
        return context


def add_to_favorites(request, id):
    movie_info = get_movie_info_by_id(id)

    if Movie.objects.filter(imdbID=id):
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))

    try:
        Movie.objects.create(
            Title=movie_info["Title"],
            Year=movie_info["Year"],
            Type=movie_info["Type"],
            imdbID=movie_info["imdbID"],
        )
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
    except TypeError:
        error = movie_info["Error"]
        return HttpResponseNotFound(f"Can't find movie with id:{error}")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/registration.html", {"form": form})


def show_favorites(request):
    movies = Movie.objects.all()
    return render(request, "favorites.html", {"favorites": movies})
