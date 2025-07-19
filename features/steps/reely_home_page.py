from behave import given, when, then, step
from selenium.webdriver.common.by import By

@when("click on off-plan menu button")
def click_off_plan(context):
    context.app.main_page.click_off_plan()