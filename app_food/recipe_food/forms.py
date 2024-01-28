from django import forms
from .models import RecipeDish, MassProduct


class FormRecipeDish(forms.ModelForm):
    class Meta:
        model = RecipeDish
        fields = '__all__'

class FormMassProduct(forms.ModelForm):
    class Meta:
        model = MassProduct
        fields = '__all__'
