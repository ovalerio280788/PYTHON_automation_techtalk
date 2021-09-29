from behave import step, use_step_matcher

from gui.features.pages.login import LoginPage
from gui.features.pages.my_account import MyAccountPage

use_step_matcher('re')


@step('I fill the (username|password) field with value (.*)')
def i_fill_username_field_with_value(context, field, value):
    page = LoginPage(context)
    field = page.username if field == 'username' else page.password
    field.send_keys(value)


@step('I click on Log In button')
def i_click_on_log_in_button(context):
    LoginPage(context).login_btn.click()


@step('I should see an error message with text (.*)')
def i_should_see_an_error_message_with_text(context, error_message):
    page = LoginPage(context)
    assert page.error_message.is_displayed(), "The error message was not displayed"
    assert page.error_message.text == error_message, f"The error message content was not the expected!!"


@step('I log in with valid credentials')
def i_login_with_valid_credentials(context):
    page = MyAccountPage(context)
    try:
        page.driver.implicitly_wait(5)
        context.execute_steps('When I visit the login page')
        if page.my_account_content is None:
            context.execute_steps(f'''
                When I fill the username field with value {context.username}
                And I fill the password field with value {context.password}
                And I click on Log In button
            ''')
    finally:
        page.driver.implicitly_wait(context.config.userdata.get('default_implicit_time'))


@step('I should see the login message "(.*)"')
def i_should_see_message_with_text(context, message):
    page = MyAccountPage(context)
    assert page.my_account_content.text == message, f'The login message {message} was not displayed!!'


@step('I should not see the username and password fields')
def i_should_not_see_the_username_and_password_fields(context):
    page = LoginPage(context)
    try:
        page.driver.implicitly_wait(5)
        assert not page.username and not page.password, "Username and password fields are still present!!"
    finally:
        page.driver.implicitly_wait(context.config.userdata.get('default_implicit_time'))
