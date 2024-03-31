from django.db import models
from django.conf import settings


class BrandCompany(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductService(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SocialMediaUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class SocialMediaPost(models.Model):
    content = models.TextField()
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(SocialMediaUser, on_delete=models.CASCADE)
    products_services = models.ManyToManyField(ProductService)

    def __str__(self):
        return self.content[:50]  # Display first 50 characters of content


class UserInteraction(models.Model):
    INTERACTION_CHOICES = [
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('share', 'Share'),
    ]
    user = models.ForeignKey(SocialMediaUser, on_delete=models.CASCADE)
    post = models.ForeignKey(SocialMediaPost, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=10, choices=INTERACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.interaction_type} - {self.post}"
