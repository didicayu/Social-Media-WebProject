# register_company.py
from behave import *
from django.contrib.auth.models import User
from myapp.models import Company

use_step_matcher("parse")

@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    User.objects.create_user(username=username, password=password)

@when('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('login'))
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    context.browser.find_by_css('input[type="submit"]').click()

@when('I register company')
def step_impl(context):
    context.browser.visit(context.get_url('company'))
    for row in context.table:
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
    context.browser.find_by_css('input[type="submit"]').click()

@then('I\'m viewing the details page for company by "{username}"')
def step_impl(context, username):
    assert context.browser.url == context.get_url('company_detail', context.get_company_id(username))

@then('There are {count:d} Companies')
def step_impl(context, count):
    assert count == Company.objects.count()

@when('I\'m not logged in')
def step_impl(context):
    context.browser.visit(context.get_url('logout'))

@then('I\'m redirected to the login form')
def step_impl(context):
    assert context.browser.url == context.get_url('login')
