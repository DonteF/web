from django.shortcuts import render
from .models import *
from django.db.models import Q, Count
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login 
from django.http import Http404, JsonResponse, HttpRequest, HttpResponse

YOUTUBE_API_KEY = "AIzaSyCHbx-cBJIp2SvgXEqDT6OBX2yCkwzLwzA"

# Create your views here.
def home(request):
    return render(request, 'recipemaker/home.html')

def search(request):
    term = request.GET.get('search')
    recipes = Recipes.objects.filter(Q(name__icontains=term)).distinct()[:4]
    recipe1 = recipes[0]
    if recipes.count() >= 2:
        recipe2 = recipes[1]
    else:
        recipe2 = None
    if recipes.count() >= 3:
        recipe3 = recipes[2]
    else:
        recipe3 = None

    if recipes.count() >= 4:
        recipe4 = recipes[3]
    else:
        recipe4 = None
    return render(request, 'recipemaker/search.html', {'recipe1': recipe1, 'recipe2': recipe2,  'recipe3': recipe3, 'recipe4': recipe4 })

def potroastrecipe(request):
    recipe = Recipes.objects.filter(Q(name__icontains='pot roast')).distinct()[:1]
    print(recipe)
    return render(request, 'recipemaker/potroastrecipe.html', {'recipe': recipe})

def chickenbreastrecipe(request):
    recipe = Recipes.objects.filter(Q(name__icontains='chicken')).distinct()[:1]
    print(recipe)
    return render(request, 'recipemaker/chickenbreastrecipe.html', {'recipe': recipe})

def ovenroastporkrecipe(request):
    recipe = Recipes.objects.filter(Q(name__icontains='pork')).distinct()[:1]
    return render(request, 'recipemaker/ovenroastporkrecipe.html', {'recipe': recipe})

def searingvideo(request):
    recipes = Recipes.objects.filter(Q(name__icontains='pot roast')).distinct()[:1]
    recipe = recipes[0]
    return render(request, 'recipemaker/searingvideo.html', {'recipe': recipe})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
            view =  super(SignUp, self).form_valid(form)
            username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
            user = authenticate(username= username, password=password)
            login(self.request, user)
            return view

def savedrecipe(request):
    name = request.POST['recipe']
    recipes = Recipes.objects.filter(Q(name__icontains=name)).distinct()[:1]
    recipe = recipes[0]
    savedstatus =  'Save'


    if request.user.is_authenticated:
        user = request.user
        saved = SavedRecipe.objects.all().filter(userid=user) & SavedRecipe.objects.all().filter(recipeid=recipe) 

        if  saved.exists():
            saved[0].delete()
            savedstatus = 'save'


        else:
            saved  = SavedRecipe.objects.all().filter(userid=user) & SavedRecipe.objects.all().filter(recipeid=recipe)

            if  saved.exists():
                  saved [0].delete()
            saved =  SavedRecipe(userid=user, recipeid=recipe)
            saved.save()
            savedstatus = 'Saved'

    return JsonResponse({'text' : savedstatus})

def sirloinRoastrecipe(request):
    recipe = Recipes.objects.filter(Q(name__icontains='sirloin')).distinct()[:1]
    return render(request, 'recipemaker/sirloinRoastrecipe.html', {'recipe': recipe})

    

def saveduserrecipe(request):
    user = request.user
    number= 0 
    recipes = SavedRecipe.objects.all().filter(userid=user)[:9]

    if recipes.count() >= 1:
        recipe1 = recipes[0].recipeid
    else:
        recipe1 = None

    if recipes.count() >= 2:
        recipe2 = recipes[1].recipeid
    else:
        recipe2 = None

    if recipes.count() >= 3:
        recipe3 = recipes[2].recipeid
    else:
        recipe3 = None

    if recipes.count() >= 4:
        recipe4 = recipes[3].recipeid
    else:
        recipe4 = None
    
    if recipes.count() >= 5:
        recipe5 = recipes[4].recipeid
    else:
        recipe5 = None

    if recipes.count() >= 6:
        recipe6 = recipes[5].recipeid
    else:
        recipe6 = None

    return render(request, 'recipemaker/saveduserrecipe.html', {'recipe1': recipe1, 'recipe2': recipe2, 'recipe3': recipe3} )
    




