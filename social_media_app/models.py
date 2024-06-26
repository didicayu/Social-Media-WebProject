from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class BrandCompany(models.Model):
    """
    Model representing a brand or company.

    Attributes:
        name (str): The name of the brand or company.
        industry (str): The industry to which the brand or company belongs.
    """

    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductService(models.Model):
    """
    Model representing a product or service.

    Attributes:
        name (str): The name of the product or service.
        category (str): The category or type of the product or service.
    """
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    company = models.ForeignKey(BrandCompany, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class SocialMediaPost(models.Model):
    """
    Model representing a social media post.

    Attributes:
        content (str): The content of the post.
        likes (int): The number of likes the post has received.
        shares (int): The number of shares the post has received.
        comments (int): The number of comments the post has received.
        timestamp (datetime): The timestamp of when the post was created.
        user (User): The user who created the post.
        product(ManyToManyField): The products or services mentioned in the post.
    """
    content = models.TextField()
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductService, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:50]  # Display first 50 characters of content


class UserInteraction(models.Model):
    """
    Model representing a user's interaction with a social media post.

    Attributes:
        INTERACTION_CHOICES (list): Choices for types of interactions.
        user (User): The user who interacted with the post.
        post (SocialMediaPost): The post being interacted with.
        interaction_type (str): The type of interaction (like, comment, share).
        timestamp (datetime): The timestamp of the interaction.
    """
    INTERACTION_CHOICES = [
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('share', 'Share'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(SocialMediaPost, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=10, choices=INTERACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.interaction_type} - {self.post}"
