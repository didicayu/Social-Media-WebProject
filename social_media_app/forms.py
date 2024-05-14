from django.forms import ModelForm
from social_media_app.models import *
from django import forms
from .models import *

class CompanyForm(forms.ModelForm):
    class Meta:
        model = BrandCompany
        exclude = ()

class SocialMediaPostForm(forms.ModelForm):
    class Meta:
        model = SocialMediaPost
        exclude = ()

class InteractionForm(forms.ModelForm):
    class Meta:
        model = UserInteraction
        exclude = ()

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductService
        exclude = ('name', 'category', 'company',)
