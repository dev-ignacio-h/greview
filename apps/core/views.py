import random 
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.template import loader
from django.views.generic import ListView
from .models import Post, SocialNetworks, Web
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def consulta(id):

    try:
        return Post.objects.get(id = id)
    except:
        return None

def getNetworks():
    return SocialNetworks.objects.filter(state = True).latest('creation_date')

def getWeb():
    return Web.objects.filter(state = True).latest('creation_date')
    
class Home(ListView):
    def get(self, request, *args, **kwargs):
        posts = list(Post.objects.filter(
            state = True,
            published = True
            ).values_list('id', flat = True))
        principal = random.choice(posts)
        posts.remove(principal)
        principal = consulta(principal)

        post1 = random.choice(posts)
        posts.remove(post1)

        post2 = random.choice(posts)
        posts.remove(post2)
        
        post3 = random.choice(posts)
        posts.remove(post3)

        post4 = random.choice(posts)
        posts.remove(post4)

        post5 = random.choice(posts)
        posts.remove(post5)
       

        context = {
            'principal': principal,
            'post1': consulta(post1),
            'post2': consulta(post2),
            'post3': consulta(post3),
            'post4': consulta(post4),
            'post5': consulta(post5),
            'socials': getNetworks(),
            'web': getWeb(),
                        
        }
        return render(request, 'home.html', context)

def signin(request):
    data = {
        'form': CustomUserForm()
    }

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            # autenticar al usuario y redirigirlo al home
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')
    return render(request, 'registration/signin.html', data)



# Create your views here.
