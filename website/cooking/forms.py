from django.forms import ModelForm
from .models import Appliance, Ingredient

class ApplianceForm(ModelForm):
    class Meta:
        model = Appliance
        fields = ('name', 'description', 'heat setting')

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name', 'description', 'cooking method')