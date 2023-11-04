from django.urls import path
from . import views


urlpatterns = [
    #path function defines a url pattern
    #'' is empty to represent based path to app
    # views.index is the function defined in views.py
    # name='index' parameter is to dynamically create url
    # example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('ingredients/', views.IngredientListView.as_view(), name = 'ingredients'),
    path('ingredient/<int:pk>', views.IngredientDetailView.as_view(), name = 'ingredient-detail'),
    path('appliances/', views.IngredientListView.as_view(), name = 'appliances'),
    path('appliance/<int:pk>', views.IngredientDetailView.as_view(), name = 'appliance-detail'),
]
