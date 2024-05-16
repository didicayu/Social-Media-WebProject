"""
URL configuration for social_media_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, DetailView
###########   from social_media_app.models import *
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),



    path('create/',
         GeneralCreateView.as_view(),
         name='create_page'),

    path('edit/',
         GeneralEditView.as_view(),
         name='edit_page'),




    path('company/create/',
         BrandCompanyCreateView.as_view(),
         name='company_create'),

    path('company/<int:pk>/',
         BrandCompanyDetailView.as_view(),
         name='company_detail'),

    path('company/<int:pk>/edit/',
         BrandCompanyUpdateView.as_view(),
         name='company_edit'),

    path('deleteCompany/<int:pk>/',
         BrandCompanyDeleteView.as_view(),
         name='company_confirm_delete'),




    path('product/create/',
         ProductCreateView.as_view(),
         name='product_create'),

    path('product/<int:pk>/',
         ProductDetailView.as_view(),
         name='product_detail'),

    path('product/<int:pk>/edit/',
         ProductUpdateView.as_view(),
         name='product_edit'),

    path('deleteProduct/<int:pk>/',
         ProductDeleteView.as_view(),
         name='product_confirm_delete'),




    path('post/create/',
         PostCreateView.as_view(),
         name='post_create'),

    path('post/<int:pk>/',
         PostDetailView.as_view(),
         name='post_detail'),

    path('post/<int:pk>/edit/',
         PostUpdateView.as_view(),
         name='post_edit'),

    path('deletePost/<int:pk>/',
         PostDeleteView.as_view(),
         name='post_confirm_delete'),




    path('interaction/<int:pk>/',
         InteractionDetailView.as_view(),
         name='interaction_detail'),
    path('interaction/create/',
         InteractionCreateView.as_view(),
         name='interaction_create'),
    path('deleteInteraction/<int:pk>/',
         InteractionDeleteView.as_view(),
         name='interaction_confirm_delete'),
    path('trending/', trending_reddit_posts, name='trending'),
]

