
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

@when('I remove post')
def step_impl(context):
    # Check if the user is logged in
    if context.browser.is_text_present('Log Out'):
        # Continue with the removal process
        q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
        query = reduce(operator.and_, q_list)
        post = SocialMediaPost.objects.filter(query).get()
        expected_url = reverse('post_confirm_delete', kwargs={'pk': post.pk})
        context.browser.visit(context.get_url(expected_url))

        context.browser.find_by_id('post_delete').click()