from django.shortcuts import render
from django.views.generic.edit import CreateView, DetailView
from django.urls import reverse_lazy
from .models import BrandCompany

class BrandCompanyCreateView(CreateView):
    model = BrandCompany
    template_name = 'brandcompany_form.html'
    fields = ['name', 'industry']

    def get_success_url(self):
        return reverse_lazy('company_detail', kwargs={'pk': self.object.pk})

class BrandCompanyDetailView(DetailView):
    model = BrandCompany
    template_name = 'brandcompany_detail.html'
    context_object_name = 'company'