from behave import given, when, then, step

@when("click first off-plan listing")
def click_first_off_plan_listing(context):
    context.app.off_plan_page.click_first_listing()

@then("verify visualization options {option}")
def verify_visualization_options_text(context,option):
    context.app.off_plan_page.check_visualization_option(option)