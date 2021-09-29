from time import sleep

from behave import when, use_step_matcher
from retrying import retry

from gui.features.pages.product_details import ProductDetailsPage
from gui.features.pages.shop import ShopPage
from gui.features.utils.botstyle import write_in_field, wait_for_element_to_be_enable, mouse_over

use_step_matcher('re')


@when('I select a product color (Blue|Green|Red) in product details page')
@retry(stop_max_attempt_number=2, wait_fixed=1000)
def i_select_a_product_with_name_from_shopping_page(context, color):
    ProductDetailsPage(context).product_color.select_by_visible_text(color)


@when('I want the product with(out)? logo')
@retry(stop_max_attempt_number=2, wait_fixed=1000)
def i_select_a_product_with_name_from_shopping_page(context, no_logo):
    ProductDetailsPage(context).product_logo.select_by_visible_text('No' if no_logo else 'Yes')


@when('I select a quantity of (\\d+)')
@retry(stop_max_attempt_number=2, wait_fixed=1000)
def i_select_a_product_with_name_from_shopping_page(context, quantity):
    page = ProductDetailsPage(context)
    write_in_field(page.product_quantity, quantity, clear=True)


@when('I get the product price')
def i_select_a_product_with_name_from_shopping_page(context):
    sleep(1)
    if hasattr(context, 'product_prices'):
        context.product_prices.append(ProductDetailsPage(context).product_price.text.split()[-1])
    else:
        context.product_prices = ProductDetailsPage(context).product_price.text.split()[-1]


@when('I click on add to cart button in product details page')
def i_select_a_product_with_name_from_shopping_page(context):
    page = ProductDetailsPage(context)
    mouse_over(context.driver, page.add_to_cart_btn)
    page.add_to_cart_btn.click()
    sleep(1)
