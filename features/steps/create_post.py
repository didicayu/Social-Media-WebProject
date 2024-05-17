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

@when('I create post')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('post_create'))
        if context.browser.url == context.get_url('post_create'):
            form = context.browser.find_by_id('post_create_form')
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('create').first.click()
@when('I create post with product "{product}"')
def step_impl(context,product):
    product = ProductService.objects.get(name=product)
    for row in context.table:
        context.browser.visit(context.get_url('post_create'))
        if context.browser.url == context.get_url('post_create'):
            form = context.browser.find_by_id('post_create_form')
            for heading in row.headings[:1]:
                context.browser.fill(heading, row[heading])
            context.browser.select("product", product.id)
            form.find_by_value('create').first.click()



@then('I\'m viewing the details page for post "{post}"')
def step_impl(context, post):
    pt  = SocialMediaPost.objects.get(content=post)
    actual_url = context.browser.url
    expected_url = context.get_url(product_id=pt.pk)
    expected_url += reverse('post_detail', kwargs={'pk': pt.pk})

    assert actual_url == expected_url

@then('There are {count:d} Posts')
def check_product_count(context, count):
    assert SocialMediaPost.objects.count() == count, f"Expected {count} posts, but got {SocialMediaPost.objects.count()}"