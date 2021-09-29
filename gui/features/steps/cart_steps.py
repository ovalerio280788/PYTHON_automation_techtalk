from behave import when, then, use_step_matcher

from gui.features.pages.cart import CartPage
from gui.features.utils.custom_web_elements.table import Table
import re

use_step_matcher('re')


@when('I add product(s)? to the cart with parameters')
def i_fill_username_field_with_value(context, products_flag):
    context.product_prices = []
    for row in context.table:
        context.execute_steps(f'''
            When I visit the shop page
            And I select a product with name {row['Name']} from shopping page
            And I select a product color {row['Color']} in product details page
            And I want the product with{'out' if row['Logo'] == 'No' else ''} logo
            And I select a quantity of {row['Items']}
            And I get the product price
            And I click on add to cart button in product details page
        ''')


@then('I should see (these|this) product(s)? added in the table')
def i_should_see_this_product_added_in_the_table(context, these_this_flag, many_products_flag):
    page = CartPage(context)
    table = Table(page.products_table)
    ui_rows = table.body_rows()
    ui_rows = [r for r in ui_rows if r.get_attribute('class') != ""]
    assert len(ui_rows) == len(context.table.rows), f'There should be "{len(context.table.rows)}" ' \
                                                    f'product(s) in the cart, but there are "{len(ui_rows)}"'

    # for ui_row in ui_rows:
    for i, test_row in enumerate(context.table):
        assert test_row['Product'] == table.get_cell_from_row(ui_rows[i])[2].text, "Good fail message here"
        assert context.product_prices[i] == table.get_cell_from_row(ui_rows[i])[3].text, "Good fail message here"
        assert test_row['Quantity'] == page.quantity_from_table_cell(table.get_cell_from_row(ui_rows[i])[4]).get_attribute('value'), \
            "Good fail message here"
        assert float("".join(re.findall('[0-9\\.]', context.product_prices[i]))) * int(test_row['Quantity']) == \
               float("".join(re.findall('[0-9\\.]', table.get_cell_from_row(ui_rows[i])[5].text))), "Good fail message here"
