from django.shortcuts import render
from recipe.forms import SearchForm
from recipe.models import Info

def display(request):
    error = False
   
    if 'recipe_name' in request.GET:
       q = request.GET['recipe_name']
       if not q:
            error = True
       else:
            val = Info.objects.filter(recipe_name=q)
            return render(request, 'disp.html', {'list': val, 'query': q})
    
    
    return render(request, 'forms.html',{'error':error,'form':form})   

def form(request):
    form = SearchForm()
    return render(request,'forms.html',{'form':form}) 

