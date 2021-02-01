from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.response import TemplateResponse
from django.views.generic import TemplateView

from MainApp.services import get_movie_info


class MainView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = {
            'movie_info': get_movie_info(),
        }
        return context

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})
