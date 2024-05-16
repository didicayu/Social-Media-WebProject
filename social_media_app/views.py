from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect
from .models import *
import tweepy
from django.http import JsonResponse
from django.conf import settings


class GeneralCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'create_page.html'
    # def post(self, request, *args, **kwargs):
    #     object_type = request.POST.get('object_type')
    #     if object_type == 'company':
    #          return redirect(reverse_lazy('company_create'))
    #     elif object_type == 'product':
    #          return redirect(reverse_lazy('product_create'))
    #     elif object_type == 'post':
    #         return redirect(reverse_lazy('post_create'))
    #     else:
    #         # Handle the case where the object type is not recognized
    #         pass


class GeneralEditView(LoginRequiredMixin, TemplateView):
    template_name = 'edit_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch all companies initially because the company dropdown is always visible
        context['companies'] = BrandCompany.objects.all()
        context['products'] = ProductService.objects.all()
        context['posts'] = SocialMediaPost.objects.all()
        context['interactions'] = UserInteraction.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        object_type = request.POST.get('object_type')

        # Redirect to different URLs based on the selected object type
        if object_type == 'product':
            selected_product_id = request.POST.get('product')
            if selected_product_id:
                redirect_url = reverse_lazy('product_detail', kwargs={'pk': selected_product_id})
                return HttpResponseRedirect(redirect_url)

        if object_type == 'company':
            selected_company_id = request.POST.get('company')
            if selected_company_id:
                redirect_url = reverse_lazy('company_detail', kwargs={'pk': selected_company_id})
                return HttpResponseRedirect(redirect_url)

        if object_type == 'post':
            selected_post_id = request.POST.get('post')
            if selected_post_id:
                redirect_url = reverse_lazy('post_detail', kwargs={'pk': selected_post_id})
                return HttpResponseRedirect(redirect_url)

        if object_type == 'interaction':
            selected_interaction_id = request.POST.get('interaction')
            if selected_interaction_id:
                redirect_url = reverse_lazy('interaction_detail', kwargs={'pk': selected_interaction_id})
                return HttpResponseRedirect(redirect_url)

        else:
            # Handle the case where the object type is not recognized
            # For example, redirect to the home page
            return HttpResponseRedirect(reverse_lazy('home'))


#####BRAND COMPANIES
class BrandCompanyCreateView(LoginRequiredMixin, CreateView):
    model = BrandCompany
    template_name = 'company_form.html'
    fields = ['name', 'industry']

    def get_success_url(self):
        print(self.object.pk)
        return reverse_lazy('company_detail', kwargs={'pk': self.object.pk})


class BrandCompanyDetailView(DetailView):
    model = BrandCompany
    template_name = 'company_detail.html'
    context_object_name = 'company'

    def get_success_url(self):
        return reverse_lazy('home')


class BrandCompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = BrandCompany
    template_name = 'company_edit.html'
    fields = ['name', 'industry']

    def get_success_url(self):
        return reverse_lazy('company_detail', kwargs={'pk': self.object.pk})


class BrandCompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = BrandCompany
    template_name = 'company_confirm_delete.html'
    success_url = reverse_lazy('home')


####PRODUCTS VIEWS
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


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductService
    template_name = 'product_edit.html'
    fields = ['name', 'category', 'company']

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.pk})


class ProductDetailView(DetailView):
    model = ProductService
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductService
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('home')


####POSTS VIEWS
class PostCreateView(LoginRequiredMixin, CreateView):
    model = SocialMediaPost
    template_name = 'post_form.html'
    fields = ['content', 'product']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.product = form.cleaned_data['product']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})


class PostDetailView(DetailView):
    model = SocialMediaPost
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = SocialMediaPost
    template_name = 'post_edit.html'
    fields = ['content', 'product']

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = SocialMediaPost
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('home')


###INTERACTION VIEWS
class InteractionCreateView(LoginRequiredMixin, CreateView):
    model = UserInteraction
    template_name = 'interaction_form.html'
    fields = ['post', 'interaction_type']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = form.cleaned_data['post']
        form.instance.interaction_type = form.cleaned_data['interaction_type']

        post = form.instance.post
        if form.instance.interaction_type == 'like':
            post.likes += 1
        elif form.instance.interaction_type == 'comment':
            post.comments += 1
        elif form.instance.interaction_type == 'share':
            post.shares += 1
        post.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('interaction_detail', kwargs={'pk': self.object.pk})


class InteractionDetailView(DetailView):
    model = UserInteraction
    template_name = 'interaction_detail.html'
    context_object_name = 'interaction'


class InteractionDeleteView(LoginRequiredMixin, DeleteView):
    model = UserInteraction
    template_name = 'interaction_confirm_delete.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        if "action" in request.POST and request.POST["action"] == "delete":
            # Perform the delete operation
            return self.delete(request, *args, **kwargs)
        else:
            # If no delete action, redirect back to the success URL
            return HttpResponseRedirect(self.success_url)

    def delete(self, request, *args, **kwargs):
        # Get the interaction instance
        interaction = self.get_object()

        # Get the post related to the interaction
        post = interaction.post

        print("Initial likes:", post.likes)
        print("Initial comments:", post.comments)
        print("Initial shares:", post.shares)

        # Update the post based on the interaction type
        if interaction.interaction_type == 'like':
            post.likes -= 1
        elif interaction.interaction_type == 'comment':
            post.comments -= 1
        elif interaction.interaction_type == 'share':
            post.shares -= 1

        # Log the updated counts for debugging
        print("Updated likes:", post.likes)
        print("Updated comments:", post.comments)
        print("Updated shares:", post.shares)
        # Save the updated post
        post.save()

        return super().delete(request, *args, **kwargs)


###### TRENDING FOR SHOWING TWEETS
# def trending_tweets(request):
#     # Twitter API credentials
#     api_key = settings.TWITTER_API_KEY
#     api_secret_key = settings.TWITTER_API_SECRET_KEY
#     access_token = settings.TWITTER_ACCESS_TOKEN
#     access_token_secret = settings.TWITTER_ACCESS_TOKEN_SECRET
#
#
#     # Authenticate with the Twitter API
#     auth = tweepy.OAuthHandler(api_key, api_secret_key)
#     auth.set_access_token(access_token, access_token_secret)
#     api = tweepy.API(auth)
#
#     # Fetch tweets
#     tweets = api.search_tweets(q="Python", count=10)  # Example: searching for tweets containing "Python"
#
#     # Pass tweets to the template
#     return render(request, 'trending.html', {'tweets': tweets})


# def trending_tweets(request):
#     # Twitter API credentials
#     api_key = settings.TWITTER_API_KEY
#     api_secret_key = settings.TWITTER_API_SECRET_KEY
#     bearer_token = settings.TWITTER_BEARER_TOKEN
#
#     # Initialize Tweepy client for API v2
#     client = tweepy.Client(bearer_token=bearer_token)
#
#     # Fetch tweets using Twitter API v2
#     query = "Python -is:retweet"  # Example query, adjust as needed
#     tweets = client.search_recent_tweets(query=query, max_results=10)
#
#     # Extracting necessary information from tweets
#     # Note: The structure of the response in v2 is different from v1.1
#     tweet_data = [{
#         'user': {'name': tweet['author_id']},  # You might need to fetch user details separately
#         'created_at': tweet['created_at'],
#         'text': tweet['text']
#     } for tweet in tweets.data]
#
#     # Pass tweets to the template
#     return render(request, 'trending.html', {'tweets': tweet_data})


# def trending_tweets(request):
#     # Initialize Tweepy client with bearer token
#     client = tweepy.Client(bearer_token=settings.TWITTER_BEARER_TOKEN)
#
#     # Fetch authenticated user's information
#     user_info = client.get_me(user_fields=['id', 'name', 'username', 'public_metrics'])
#
#     # Check if the request was successful
#     if user_info.data:
#         # Prepare the user information to return
#         user_data = {
#             'id': user_info.data.id,
#             'name': user_info.data.name,
#             'username': user_info.data.username,
#             'followers_count': user_info.data.public_metrics['followers_count'],
#             'following_count': user_info.data.public_metrics['following_count'],
#             'tweet_count': user_info.data.public_metrics['tweet_count'],
#         }
#         return JsonResponse(user_data, safe=False)
#     else:
#         # Handle errors or no data found
#         return JsonResponse({'error': 'User information could not be retrieved'}, status=404)


# def trending_tweets(request):
#     # Initialize Tweepy client with bearer token
#     print(settings.TWITTER_BEARER_TOKEN)
#     client = tweepy.Client(bearer_token=settings.TWITTER_BEARER_TOKEN)
#
#     # Perform a simple API call to verify functionality
#     response = client.get_me()
#
#     # Check if the request was successful
#     if response.data:
#         return JsonResponse({'message': 'API call successful', 'data': response.data}, safe=False)
#     else:
#         return JsonResponse({'error': 'API call failed', 'details': response.errors}, status=404)


import requests
from django.http import JsonResponse
from django.conf import settings


def trending_tweets(request):
    # Twitter API URL for fetching user information
    url = "https://api.twitter.com/2/users/me"

    # Headers for OAuth 2.0 Bearer Token authentication
    headers = {
        "Authorization": f"Bearer {settings.TWITTER_BEARER_TOKEN}"
    }

    # Make the GET request to the Twitter API
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        user_data = response.json()
        return JsonResponse({'message': 'API call successful', 'data': user_data}, safe=False)
    else:
        return JsonResponse({'error': 'API call failed', 'details': response.text}, status=response.status_code)