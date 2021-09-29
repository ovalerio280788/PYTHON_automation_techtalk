from behave import when, use_step_matcher
from retrying import retry

from gui.features.pages.cart import CartPage
from gui.features.pages.login import LoginPage
from gui.features.pages.shop import ShopPage

use_step_matcher('re')


@when('I visit the (login|cart|shop) page')
@retry(stop_max_attempt_number=3, wait_fixed=3000)
def i_visit_page(context, page_name):
    if page_name == 'login':
        LoginPage(context).visit()
    elif page_name == 'cart':
        CartPage(context).visit()
    elif page_name == 'shop':
        ShopPage(context).visit()
    else:
        raise Exception('Not a valid page name provided.')
