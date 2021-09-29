from behave import when, use_step_matcher

from gui.features.pages.shop import ShopPage

use_step_matcher('re')


@when('I select a product with name (.*) from shopping page')
def i_select_a_product_with_name_from_shopping_page(context, product_name):
    page = ShopPage(context)
    page.product_with_name(product_name).click()
