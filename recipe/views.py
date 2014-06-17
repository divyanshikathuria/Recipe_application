from django.shortcuts import render
from recipe.forms import SearchForm
from recipe.models import Info

def display(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data['recipe_name']
            obj= Info.objects.values('recipe_name','recipe_text', 'Ingredient1','Ingredient2','Ingredient3','Ingredient4', 'Ingredient1_cost','Ingredient2_cost','Ingredient3_cost','Ingredient4_cost').filter(id=1)
            obj1 = Info.objects.get(id=1)
            Ingredient1_cost = obj1.Ingredient1_cost
            Ingredient2_cost = obj1.Ingredient2_cost
            Ingredient3_cost = obj1.Ingredient3_cost
            Ingredient4_cost = obj1.Ingredient4_cost
            total_cost = Ingredient1_cost + Ingredient2_cost + Ingredient3_cost + Ingredient4_cost
            return render(request, 'disp.html', {'obj': obj, 'total_cost ': total_cost  })
    else:
        form = SearchForm()
        return render(request,'forms.html',{'form': form})  
