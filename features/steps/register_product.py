# features/steps/register_product.py
from behave import given, when, then
from django.contrib.auth.models import User
from django.urls import reverse
from social_media_app.models import *
from django.db.models import Q
from functools import reduce
from django.http import HttpRequest
import operator
use_step_matcher("parse")


@when('I register product')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('product_create'))
        if context.browser.url == context.get_url('product_create'):
            form = context.browser.find_by_id('product_create_form')
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('create').first.click()


@then('I\'m viewing the details page for product by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    product = ProductService.objects.filter(reduce(operator.and_, q_list)).get()
    actual_url = context.browser.url
    expected_url = context.get_url(product_id=product.pk)
    expected_url += reverse('product_detail', kwargs={'pk': product.pk})

    assert actual_url == expected_url


@then('There are {count:d} Products')
def check_product_count(context, count):
    assert ProductService.objects.count() == count, f"Expected {count} products, but got {ProductService.objects.count()}"
