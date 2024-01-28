import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from . import models
from . import forms


class RecipeDishView(ListView):
    queryset = models.RecipeDish.objects.all()
    template_name = 'recipe_dish.html'
    context_object_name = 'recipe_list'


class ProductView(ListView):
    queryset = models.Product.objects.all()
    template_name = 'product.html'
    context_object_name = 'products_list'


class FormRecipeView(CreateView):
    model = models.RecipeDish
    form_class = forms.FormRecipeDish
    template_name = 'form_recipe.html'
    success_url = '/'


class MassProductView(CreateView):
    model = models.MassProduct
    form_class = forms.FormMassProduct
    template_name = 'form_recipe.html'
    success_url = '/form_recipe'

from django.shortcuts import HttpResponse
from . import models

def add_product_to_recipe(request, recipe_id, product_id, weight):
    try:
        recipe = models.RecipeDish.objects.get(id=recipe_id)
        product = models.Product.objects.get(id=product_id)

        # Проверяем, существует ли продукт в рецепте
        mass_product = recipe.mass_product_id.filter(product_id=product).first()

        if mass_product:
            # Если продукт уже есть в рецепте, обновляем его вес
            mass_product.mass_product = weight
            mass_product.save()
        else:
            # Если продукта нет в рецепте, создаем его с указанным весом
            mass_product = models.MassProduct.objects.create(product_id=product, mass_product=weight)
            recipe.mass_product_id.add(mass_product)

        return HttpResponse("Product added to recipe successfully.")

    except models.RecipeDish.DoesNotExist:
        return HttpResponse("Recipe does not exist.")

    except models.Product.DoesNotExist:
        return HttpResponse("Product does not exist.")

    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")


def cook_recipe(request, recipe_id):
    try:
        recipe = models.RecipeDish.objects.get(id=recipe_id)

        mass_products = recipe.mass_product_id.all()

        for product in mass_products:
            product.product_id.count_cooked += 1
            product.product_id.save()

        return HttpResponse("Recipe cooked successfully.")

    except models.RecipeDish.DoesNotExist:
        return HttpResponse("Recipe does not exist.")


def show_recipes_without_product(request, product_id):
    try:
        product = models.Product.objects.get(id=product_id)
        # Получаем список рецептов, в которых продукт отсутствует или присутствует менее 10 грамм
        recipes = models.RecipeDish.objects.exclude(mass_product_id__product_id=product).distinct()
        recipes_less_than_10g = models.RecipeDish.objects.filter(mass_product_id__product_id=product,
                                                                 mass_product_id__mass_product__lt=10)
        recipes = recipes.union(recipes_less_than_10g)

        return render(request, 'recipes_without_product.html', {'recipes': recipes, 'product': product})

    except models.Product.DoesNotExist:
        return HttpResponse("Product does not exist.")


def add_product(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        name_product = body_data['name']
        if name_product:
            object_product = models.Product(name=name_product)
            try:
                object_product.save()
                data = {'succes': 'OK'}
                return JsonResponse(data)
            except Exception as e:
                data = {'error': str(e)}
                return JsonResponse(data, status=500)
        else:
            data = {'error': 'Name field is empty'}
            return JsonResponse(data)
    else:
        data = {'error': 'Only POST requests are allowed'}
        return JsonResponse(data, status=405)
