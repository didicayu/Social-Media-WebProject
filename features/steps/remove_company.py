
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

@given('Exists company registered by "{username}"')
def step_impl(context, username):
    for row in context.table:
        context.browser.visit(context.get_url('company_create'))
        if context.browser.url == context.get_url('company_create'):
            form = context.browser.find_by_id('company_create_form')
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()
    assert BrandCompany.objects.count() == 1


@when('I remove company')
def step_impl(context):
    # Check if the user is logged in
    if context.browser.is_text_present('Log Out'):
        # Continue with the removal process
        q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
        query = reduce(operator.and_, q_list)
        company = BrandCompany.objects.filter(query).get()
        expected_url = reverse('company_confirm_delete', kwargs={'pk': company.pk})
        context.browser.visit(context.get_url(expected_url))
        context.browser.find_by_id('company_delete').click()





