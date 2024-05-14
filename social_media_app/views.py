from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import *


class BrandCompanyCreateView(LoginRequiredMixin,CreateView):
    model = BrandCompany
    template_name = 'brandcompany_form.html'
    fields = ['name', 'industry']

    def get_success_url(self):
        return reverse_lazy('company_detail', kwargs={'pk': self.object.pk})

class BrandCompanyDetailView(DetailView):
    model = BrandCompany
    template_name = 'company_detail.html'
    context_object_name = 'company'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = SocialMediaPost
    template_name = 'post_form.html'
    fields = ['content','product']

    def form_valid(self, form):
        form.instance.product = form.cleaned_data['product']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

class PostDetailView(DetailView):
    model = SocialMediaPost
    template_name = 'post_detail.html'
    context_object_name = 'post'

class InteractionCreateView(LoginRequiredMixin, CreateView):
    model = UserInteraction
    template_name = 'interaction_form.html'
    fields = ['post', 'interaction_type']

    def get_success_url(self):
        return reverse_lazy('interaction_detail', kwargs={'pk': self.object.pk})


class InteractionDetailView(DetailView):
    model = BrandCompany
    template_name = 'interaction_detail.html'
    context_object_name = 'interaction'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = ProductService
    template_name = 'product_form.html'
    fields = ['name', 'category', 'company']

    def form_valid(self, form):
        # company_id = form.cleaned_data['company'].id
        # form.instance.company = BrandCompany.objects.get(id= company_id)
        form.instance.company = form.cleaned_data['company']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.pk})





class ProductDetailView(DetailView):
    model = ProductService
    template_name = 'product_detail.html'
    context_object_name = 'product'