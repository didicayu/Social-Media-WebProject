# features/steps/register_company.py
from behave import given, when, then
from django.contrib.auth.models import User
from django.urls import reverse
from social_media_app.models import *
from django.db.models import Q
from functools import reduce
from django.http import HttpRequest
import operator
use_step_matcher("parse")


@when('I register company')
def step_impl(context):
    if context.browser.is_text_present('Log Out'):
        for row in context.table:
            context.browser.visit(context.get_url('company_create'))
            if context.browser.url == context.get_url('company_create'):
                form = context.browser.find_by_id('company_create_form')
                for heading in row.headings:
                    context.browser.fill(heading, row[heading])
                form.find_by_value('Submit').first.click()


@then('I\'m viewing the details page for company by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    query = reduce(operator.or_, q_list)
    company = BrandCompany.objects.filter(query).get()
    actual_url = context.browser.url
    expected_url = context.get_url(company_id=company.pk)
    expected_url += reverse('company_detail', kwargs={'pk': company.pk})

    assert actual_url == expected_url, f"Expected to be  {expected_url} page, but was at {actual_url}"



@then('There are {count:d} Companies')
def check_company_count(context, count):
    assert BrandCompany.objects.count() == count, f"Expected {count} companies, but got {BrandCompany.objects.count()}"

