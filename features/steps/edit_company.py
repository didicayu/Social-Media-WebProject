# features/steps/edit_company.py
from behave import given, when, then
from django.contrib.auth.models import User
from django.urls import reverse
from social_media_app.models import BrandCompany
from django.db.models import Q
from functools import reduce
from splinter.exceptions import ElementDoesNotExist
import operator

use_step_matcher("parse")


@when('I edit the company with the name "{company_name}"')
def step_impl(context, company_name):
    if context.browser.is_text_present('Log Out'):
        for row in context.table:
            q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
            query = reduce(operator.and_, q_list)
            company = BrandCompany.objects.filter(query).get()
            expected_url = reverse('company_edit', kwargs={'pk': company.pk})
            context.browser.visit(context.get_url(expected_url))
            if context.browser.url == context.get_url(expected_url):
                form = context.browser.find_by_id('company_edit_form')
                for heading in row.headings:
                    if heading != 'name':
                        context.browser.fill(heading, row[heading])
                form.find_by_value('Submit').first.click()
    else:
        context.browser.visit(context.get_url('/accounts/login/'))

@when('I view the details for company "{company_name}"')
def step_impl(context, company_name):
    if context.browser.is_text_present('Log Out'):
        company = BrandCompany.objects.get(name=company_name)
        context.browser.visit(context.get_url('company_detail', company.pk))
