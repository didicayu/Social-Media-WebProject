from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import BrandCompany

class BrandCompanyCreateView(CreateView):
    model = BrandCompany
    template_name = 'brandcompany_form.html'
    fields = ['name', 'industry']
    success_url = reverse_lazy('company_list')