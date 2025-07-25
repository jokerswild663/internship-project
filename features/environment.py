from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from app.main import Application

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    ## chrome
    options=webdriver.ChromeOptions()
    # options.add_argument('--headless=new')
    # options.add_argument('--window-size=1920,1080')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--disable-web-security')
    # options.add_argument('--allow-running-insecure-content')
    # options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('useAutomationExtension', False)    # options.add_argument('--remote-debugging-port=9222')
    # options.add_argument('--remote-debugging-port=9222')
    #
    context.driver = webdriver.Chrome(
        options=options
    )


    ## firefox
    # context.driver = webdriver.Firefox()

    ## Browserstack
    # bs_user = ''
    # bs_access = ''
    # url = f'http://{bs_user}:{bs_access}@hub-cloud.browserstack.com/wd/hub'
    # options = Options()
    # options.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 0})
    # bstack_options = {
    #     "os": "OS X",
    #     "osVersion": "Monterey",
    #     "browserName": "Firefox",
    #     # "browserName": "Chrome",
    #     # "browserName": "Edge",
    #     # "browserName": "Safari",
    #     "sessionName": scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(20)
    context.driver.wait = WebDriverWait(context.driver, 20)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
