
from behave import given, when, then
from django.contrib.auth.models import User
from django.urls import reverse
from social_media_app.models import *
from django.db.models import Q
from functools import reduce
from django.http import HttpRequest
import operator
from social_media_app.models import *
use_step_matcher("parse")

@when('I remove interaction in post "{post}"')
def step_impl(context,post):
    # Check if the user is logged in
    if context.browser.is_text_present('Log Out'):
        # Continue with the removal process
        postV = SocialMediaPost.objects.get(content= post)
        interaction = UserInteraction.objects.get(post=postV.id)
        expected_url = reverse('interaction_confirm_delete', kwargs={'pk': interaction.pk})
        context.browser.visit(context.get_url(expected_url))
        context.browser.find_by_value('delete_interaction').first.click()
