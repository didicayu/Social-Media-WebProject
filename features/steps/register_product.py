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

@when('I register product with company "{company}"')
def step_impl(context,company):
    companyObj = BrandCompany.objects.get(name=company)
    #companyObj = BrandCompany.objects.get(name=company)
    for row in context.table:
        context.browser.visit(context.get_url('product_create'))
        if context.browser.url == context.get_url('product_create'):
            form = context.browser.find_by_id('product_create_form')
            for heading in row.headings[:2]:
                context.browser.fill(heading, row[heading])
                # context.browser.fill("name", "cola")
                # context.browser.fill("category", "Drink")
            context.browser.select("company", companyObj.id)
            form.find_by_value('create').first.click()




@then('I\'m viewing the details page for product "{product}"')
def step_impl(context, product):
    product  = ProductService.objects.get(name=product)
    actual_url = context.browser.url
    expected_url = context.get_url(product_id=product.pk)
    expected_url += reverse('product_detail', kwargs={'pk': product.pk})

    assert actual_url == expected_url


@then('There are {count:d} Products')
def check_product_count(context, count):
    assert ProductService.objects.count() == count, f"Expected {count} products, but got {ProductService.objects.count()}"
