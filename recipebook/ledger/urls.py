from django.urls import path
from .views import RecipeListView, RecipeDetailView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('list', RecipeListView.as_view(), name = 'list'),
    path('<int:pk>/detail', RecipeDetailView.as_view(), name='recipe_detail')
    
]

app_name = 'ledger'