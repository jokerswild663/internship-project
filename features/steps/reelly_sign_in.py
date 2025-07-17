from behave import given, when, then, step
from time import sleep

@given('open reelly {site}')
def open_sign_in(context,site):
    context.app.sign_in_page.open_sign_in_page(site)
    context.app.sign_in_page.sign_in()