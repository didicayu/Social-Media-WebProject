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

@when('I create like interaction for post "{post}"')
def step_impl(context,post):
    for row in context.table:
        pt = SocialMediaPost.objects.get(content=post)
        context.browser.visit(context.get_url('interaction_create'))
        if context.browser.url == context.get_url('interaction_create'):
            form = context.browser.find_by_id('interaction_create_form')
            # for heading in row.headings[:1]:
            #     context.browser.fill(heading, row[heading])
            context.browser.select("post", pt.id)
            context.browser.select("interaction_type", UserInteraction.INTERACTION_CHOICES[0][0])
            form.find_by_value('save').first.click()

@then('I\'m viewing the details page for interaction in post "{post}"')
def step_impl(context, post):
    for row in context.table:
        pt = SocialMediaPost.objects.get(content=post)
        interaction  = UserInteraction.objects.get(post=pt.id)
        actual_url = context.browser.url
        expected_url = context.get_url(id=interaction.pk)
        expected_url += reverse('interaction_detail', kwargs={'pk': interaction.pk})

        assert actual_url == expected_url


@then('There are {count:d} Interactions')
def check_product_count(context, count):
    assert UserInteraction.objects.count() == count, f"Expected {count} interactions, but got {UserInteraction.objects.count()}"


@then('There are {count:d} likes in post "{post}"')
def check_product_count(context, count, post):
    pt = SocialMediaPost.objects.get(content=post)
    assert pt.likes == count, f"Expected {count} likes, but got {pt.likes}"
