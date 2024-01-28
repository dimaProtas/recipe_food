from django.urls import path
from . import views


urlpatterns = [
    path('', views.RecipeDishView.as_view(), name='recipe-list'),
    path('product/', views.ProductView.as_view(), name='product-list'),
    path('form_recipe/', views.FormRecipeView.as_view(), name='form-recipe'),
    path('form_mass_product/', views.MassProductView.as_view(), name='form_mass_product'),
    path('add_product_to_recipe/<int:recipe_id>/<int:product_id>/<int:weight>/', views.add_product_to_recipe),
    path('cook_recipe/<int:recipe_id>/', views.cook_recipe),
    path('show_recipes_without_product/<int:product_id>/', views.show_recipes_without_product, name='show_recipes_without_product'),
    path('add_product/', views.add_product),
]
