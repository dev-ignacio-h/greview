import random 
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse
from django.template import loader
from django.views.generic import ListView, DetailView
from .models import Post, SocialNetworks, Web, Author, Category
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

#rest_framework

from rest_framework import viewsets
from .serializers import AuthorSerializer

def consulta(id):

    try:
        return Post.objects.get(id = id)
    except:
        return None

def consultaCategoria(name):
    try:
        return Category.objects.get(name = name)
    except:
        return None

def consultaCategoriaJuego(category):
    try:
        return Posts.objects.get(category = category)
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


class CategoryList(ListView):
    def get(self, request, *args, **kwargs):
        categories = list(Category.objects.filter(
            state = True,
            ).values_list('name'))

        adventure = Category.objects.get(name = 'Aventura')

        strategy = Category.objects.get(name = 'Estrategia')

        war = Category.objects.get(name = 'Acción Bélica')

        race = Category.objects.get(name = 'Carreras')

        mmorpg = Category.objects.get(name = 'MMORPG')

        context = {
            'adventure': consultaCategoria(adventure),
            'strategy': consultaCategoria(strategy),
            'war': consultaCategoria(war),
            'race': consultaCategoria(race),
            'mmorpg': consultaCategoria(mmorpg),
            'socials': getNetworks(),
            'web': getWeb(),
        }
        return render(request, 'categoria.html', context)

#Genero Aventura
class AdventureList(ListView):
    def get(self, request, *args, **kwargs):
        posts_adventure = Post.objects.filter(
            state = True,
            published = True,
            category = Category.objects.get(name = 'Aventura')
        )
        try:
            category = Category.objects.get(name = 'Aventura')
        except:
            category = None

        paginator = Paginator(posts_adventure, 4)
        pagina = request.GET.get('page')
        posts =paginator.get_page(pagina)
    
        context = {
            'posts': posts,
            'socials': getNetworks(),
            'web': getWeb(),
            'category' : category,
        }
        return render(request, 'genero.html', context)

#Genero Estrategia
class StrategyList(ListView):
    def get(self, request, *args, **kwargs):
        posts_strategy = Post.objects.filter(
            state = True,
            published = True,
            category = Category.objects.get(name = 'Estrategia')
        )
        try:
            category = Category.objects.get(name = 'Estrategia')
        except:
            category = None

        paginator = Paginator(posts_strategy, 4)
        pagina = request.GET.get('page')
        posts =paginator.get_page(pagina)
    
        context = {
            'posts': posts,
            'socials': getNetworks(),
            'web': getWeb(),
            'category' : category,
        }
        return render(request, 'genero.html', context)

#Genero Acción Bélica
class WarList(ListView):
    def get(self, request, *args, **kwargs):
        posts_war = Post.objects.filter(
            state = True,
            published = True,
            category = Category.objects.get(name = 'Acción Bélica')
        )
        try:
            category = Category.objects.get(name = 'Acción Bélica')
        except:
            category = None

        paginator = Paginator(posts_war, 4)
        pagina = request.GET.get('page')
        posts =paginator.get_page(pagina)
    
        context = {
            'posts': posts,
            'socials': getNetworks(),
            'web': getWeb(),
            'category' : category,
        }
        return render(request, 'genero.html', context)

#Género Carreras
class RaceList(ListView):
    def get(self, request, *args, **kwargs):
        posts_race = Post.objects.filter(
            state = True,
            published = True,
            category = Category.objects.get(name = 'Carreras')
        )
        try:
            category = Category.objects.get(name = 'Carreras')
        except:
            category = None

        paginator = Paginator(posts_race, 4)
        pagina = request.GET.get('page')
        posts =paginator.get_page(pagina)
    
        context = {
            'posts': posts,
            'socials': getNetworks(),
            'web': getWeb(),
            'category' : category,
        }
        return render(request, 'genero.html', context)

#Genero MMORPG
class MMORPGList(ListView):
    def get(self, request, *args, **kwargs):
        posts_mmorpg = Post.objects.filter(
            state = True,
            published = True,
            category = Category.objects.get(name = 'MMORPG')
        )
        try:
            category = Category.objects.get(name = 'MMORPG')
        except:
            category = None

        paginator = Paginator(posts_mmorpg, 4)
        pagina = request.GET.get('page')
        posts =paginator.get_page(pagina)
    
        context = {
            'posts': posts,
            'socials': getNetworks(),
            'web': getWeb(),
            'category' : category,
        }
        return render(request, 'genero.html', context)

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

#Detalle de los Post
class PostDetail(DetailView):
    def get(self, request, slug, *args, **kwargs):
        try:
            post = Post.objects.get(slug = slug)
        except:
            post = None
        
        context = {
            'post': post,
            'sociales': getNetworks(),
            'web': getWeb(),
        }
        return render(request, 'post.html', context)


# viewsets

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


def indicadores(request):
    return render(request, 'indicadores.html')

def pokemons(request):
    return render(request, 'pokemons.html')



# Create your views here.
