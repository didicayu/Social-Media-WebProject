import random
import os
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from dotenv import load_dotenv
import praw


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


###### TRENDING FOR SHOWING POSTS FROM REDDIT

def trending_reddit_posts(request):
    if request.method == 'POST':
        placeholder_user = User.objects.get_or_create(username=request.POST.get('author'))[0]
        placeholder_product = ProductService.objects.get_or_create(name='placeholder_product')[0]

        post_data = {
            'content': f"{request.POST.get('title')} - {request.POST.get('url')}",
            'likes': int(request.POST.get('score')),
            'shares': 0,  # Assuming no shares data
            'comments': int(request.POST.get('comments')),
            'user': placeholder_user,
            'product': placeholder_product
        }
        SocialMediaPost.objects.create(**post_data)

        return HttpResponse('<script>alert("Post saved successfully!"); window.location.href = "{% url \'home\' %}"</script>')

    else:
        load_dotenv()

        client_id = os.getenv('REDDIT_CLIENT_ID')
        client_secret = os.getenv('REDDIT_CLIENT_SECRET')
        user_agent = os.getenv('REDDIT_USER_AGENT')
        username = os.getenv('REDDIT_USERNAME')
        password = os.getenv('REDDIT_PASSWORD')

        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
            username=username,
            password=password
        )

        subreddit_name = request.GET.get('subreddit')

        try:
            subreddit = reddit.subreddit(subreddit_name)
            top_posts = subreddit.top(limit=10)
            posts_data = [{
                'title': post.title,
                'url': post.url,
                'author': post.author.name if post.author else 'Unknown',
                'score': post.score,
                'comments': post.num_comments
            } for post in top_posts]

        except Exception as e:
            popular_subreddits = reddit.subreddits.popular()
            popular_subreddits_list = list(popular_subreddits)
            subreddit = random.choice(popular_subreddits_list)
            subreddit.title += f"</br> The subreddit {subreddit_name} was not found! - Showing Random Posts"
            top_posts = subreddit.top(limit=10)

            posts_data = [{
                'title': post.title,
                'url': post.url,
                'author': post.author.name if post.author else 'Unknown',
                'score': post.score,
                'comments': post.num_comments
            } for post in top_posts]

        return render(request, 'trending.html', {'posts': posts_data, 'subreddit_title': subreddit.title})
