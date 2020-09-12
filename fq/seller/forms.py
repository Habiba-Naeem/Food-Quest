from django import forms
from .models import Dish


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Dish
        fields = ('picture',)