# features/steps/edit_product.py
from behave import given, when, then
from django.contrib.auth.models import User
from django.urls import reverse
from social_media_app.models import *
from django.db.models import Q
from functools import reduce
from splinter.exceptions import ElementDoesNotExist
import operator

use_step_matcher("parse")


@when('I edit the product with the name "{product}"')
def step_impl(context, product):
    if context.browser.is_text_present('Log Out'):
        for row in context.table:
            prod = ProductService.objects.get(name=product)
            expected_url = reverse('product_edit', kwargs={'pk': prod.pk})
            context.browser.visit(context.get_url(expected_url))
            if context.browser.url == context.get_url(expected_url):
                form = context.browser.find_by_id('product_edit_form')
                for heading in row.headings:
                    context.browser.fill(heading, row[heading])
                form.find_by_value('Submit').first.click()
    else:
        context.browser.visit(context.get_url('/accounts/login/'))
