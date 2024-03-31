from django.contrib import admin
from .models import BrandCompany, ProductService, SocialMediaUser, SocialMediaPost, UserInteraction

# Register your models here.
admin.site.register(BrandCompany)
admin.site.register(ProductService)
admin.site.register(SocialMediaUser)
admin.site.register(SocialMediaPost)
admin.site.register(UserInteraction)