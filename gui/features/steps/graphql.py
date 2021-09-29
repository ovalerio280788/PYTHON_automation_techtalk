import jmespath
from behave import when, then, use_step_matcher
import re

from gui.features.utils.graphql.gqllib import execute_gql
from gui.features.utils.graphql.queries import *

use_step_matcher('re')


@when('I send query with name (.*)')
def i_select_a_product_with_name_from_shopping_page(context, query_name):
    query = eval(query_name)
    execute_gql(context, query)


@then('The status code should be (\\d+)')
def the_status_code_should_be(context, status_code):
    context.logger.debug(f"Verifying status code: Expected: {status_code} / Got: {context.graphql.result.extensions['status_code']}")
    assert context.graphql.result.extensions['status_code'] == int(status_code), \
        f"Expected status code [ {status_code} ] but found [ {context.graphql.result.extensions['status_code']} ]!!"


@then('The response json should have (these errors|this data|these keys)')
def the_response_json_should_have(context, flag):
    for row in context.table:
        if flag == 'these errors':
            assert str(context.graphql.result.errors[0][row['key']]) == str(row['value']), \
                f"The expected error is not found!!. " \
                f"Actual: {str(context.graphql.result.errors[0][row['key']])} -- " \
                f"Expected: {str(row['value'])}"
        elif flag == 'these keys':
            context.logger.debug(f"Checking key '{row['expected_key']}' to be into '{context.graphql.result.data}'")
            assert jmespath.search(row['expected_key'], context.graphql.result.data) is not None, \
                f"Key '{row['expected_key']}' no in '{context.graphql.result.data}' as expected!!"
            context.logger.debug("--> OK")
        else:
            assert str(context.graphql.result.data[row['key']]) == str(row['value']), \
                f"The expected data is not found!!. " \
                f"Actual: {str(context.graphql.result.data[row['key']])} -- " \
                f"Expected: {str(row['value'])}"


@then('Each (.*) into json node (.*) should have a (int|string|string or null|float|float or int|float or null or int) value( with format (.*))?')
def each_key_into_json_node_should_have_type_value(context, key, json_node, data_type, flag_with_format, string_format):
    context.logger.debug(f"Checking key '{key}' into json node '{json_node}' has a data type '{data_type}'")
    base_node = jmespath.search(key, context.graphql.result.data)
    for node in base_node:
        if data_type == "int":
            assert type(node) == int, f"key '{key}', but it is not!!"
        elif data_type == "float":
            assert type(node) == float, f"key '{key}', but it is not!!"
        elif data_type == "float or int":
            assert type(node) == float or type(node) == int, f"key '{key}', but it is not!!"
        elif data_type == "float or null or int":
            assert node is None or type(node) == float or type(node) == int, f"key '{key}', but it is not!!"
        elif data_type == "string or null":
            assert node is None or type(node) == str, f"key '{key}', but it is not!!"
        else:
            assert type(node) == str, f"key '{key}', but it is not!!"

            if flag_with_format:
                assert re.match(string_format, node), f"The node value '{node}' do not has the format '{string_format}'"
    context.logger.debug("--> OK [No data returned this time by the query]" if not base_node else "--> OK")


@then('The response time should be less than (\\d+) ms')
def the_response_time_should_be_less_than(context, time_in_ms):
    context.logger.info(f"The request took: {context.graphql.result.extensions['response_elapsed'].microseconds / 1000} ms")
    assert context.graphql.result.extensions['response_elapsed'].microseconds / 1000 < float(time_in_ms)
