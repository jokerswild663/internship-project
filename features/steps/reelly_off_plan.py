from behave import given, when, then, step

@when("click first off-plan listing")
def click_first_off_plan_listing(context):
    context.app.off_plan_page.click_first_listing()

@then("verify visualization options")
def verify_visualization_options_text(context):
    options = ['Architecture','Interior','Lobby']
    context.app.off_plan_page.verify_visualization_options(options)