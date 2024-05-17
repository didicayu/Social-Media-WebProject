# features/steps/edit_company.py
from behave import given, when, then
from django.contrib.auth.models import User
from django.urls import reverse
from social_media_app.models import *
from django.db.models import Q
from functools import reduce
from splinter.exceptions import ElementDoesNotExist
import operator

use_step_matcher("parse")

@when('I edit the post "{post}"')
def step_impl(context, post):
    if context.browser.is_text_present('Log Out'):
        for row in context.table:
            pt  = SocialMediaPost.objects.get(content=post)
            expected_url = reverse('post_edit', kwargs={'pk': pt.pk})
            context.browser.visit(context.get_url(expected_url))
            if context.browser.url == context.get_url(expected_url):
                form = context.browser.find_by_id('post_edit_form')
                for heading in row.headings:
                    if heading != 'product':
                        context.browser.fill(heading, row[heading])
                form.find_by_value('Submit').first.click()
    else:
        context.browser.visit(context.get_url('/accounts/login/'))


