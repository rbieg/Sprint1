from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import IngredientForm, ApplianceForm
from django.contrib import messages
# Create your views here.

def delete_appliance(request, appliance_id):
    appliance = Appliance.objects.get(pk=appliance_id)
    return render(request, 'cooking/appliance_confirm_delete.html', {'appliance': appliance})
def update_appliance(request, appliance_id):
    appliance = Appliance.objects.get(pk=appliance_id)
    form = ApplianceForm(instance=appliance)
    if request.method == 'POST':
        form = Appliance(request.POST, instance=appliance)
        if form.is_valid():
            form.save()
            return redirect('appliance-detail', appliance_id)
    return render(request, 'cooking/appliance_form.html', {'form': form})
def update_ingredient(request, ingredient_id):
    ingredient = Ingredient.objects.get(pk=ingredient_id)
    form = IngredientForm(instance=ingredient)
    if request.method == 'POST':
        form = Appliance(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient-detail', ingredient_id)
    return render(request, 'cooking/ingrediente_form.html', {'form': form})

def index(request):
    return render(request, 'cooking/index.html')

def create_appliance(request, appliance_id):
    form = ApplianceForm() 
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        appliance_data = request.POST.copy()
        appliance_data['appliance_id'] = appliance_id
        form = ApplianceForm(appliance_data)
        if form.is_valid():
            return redirect('appliance-detail', appliance_id)
    context = {'form': form}
    return render(request, 'cooking/project_form.html', context)
    
class ApplianceListView(generic.ListView):
    model = Appliance
class ApplianceDetailView(generic.DetailView):
    model = Appliance
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class IngredientListView(generic.DetailView):
    model = Ingredient
class IngredientDetailView(generic.DetailView):
    model = Ingredient
    template_name = 'cooking/ingredient_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context