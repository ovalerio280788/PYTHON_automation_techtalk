import os

import allure
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
from behave.model_core import Status
from loguru import logger

from gui.features.utils.behave_repeated_runner import patch_scenario_with_repeat
from gui.features.utils.driver_config import setup_browser, clean_browser

# https://behave.readthedocs.io/en/latest/api.html?highlight=before_feature#environment-file-functions
from gui.features.utils.graphql.gqllib import connect_to_graphql, execute_gql
from gui.features.utils.graphql.queries import EMPTY_CART
from gui.features.utils.singleton import singleton_instances


def before_all(context):
    context.logger = logger
    context.logger.add(
        "logs/ui_testing_{time}.log",
        rotation="500 MB",
        compression="zip",
        colorize=True,
        format="<green>{time}</green> <level>{message}</level>",
        level=context.config.userdata.get('loglevel') or "INFO"
    )
    context.implicit_wait = context.config.userdata.get('default_implicit_time')
    context.timeout = context.config.userdata.get('default_page_load_time')
    context.username = context.config.userdata.get('username') or os.environ['username']
    context.password = context.config.userdata.get('password') or os.environ['password']
    # printing a summary
    context.logger.info("*" * 80)
    context.logger.info(" STARTING EXECUTION")
    context.logger.info("*" * 80)
    context.logger.info(f"      BROWSER: {context.config.userdata.get('browser')}")
    context.logger.info(f"     USERNAME: {context.username}")
    context.logger.info(f"  ENVIRONMENT: {context.config.userdata.get('ui_base_url')}")
    connect_to_graphql(context)


def before_feature(context, feature):
    for scenario in feature.walk_scenarios():
        for tag in scenario.effective_tags:
            if "retry" in tag:
                patch_scenario_with_autoretry(scenario, max_attempts=int(tag.split('_')[-1]))
        if context.config.userdata.get('repeat'):
            patch_scenario_with_repeat(scenario=scenario,
                                       logger=context.logger,
                                       max_repeat=int(context.config.userdata.get('repeat')))

    if "graphql" not in feature.tags:
        setup_browser(context)


def after_feature(context, feature):
    # Close and clean the driver
    if "graphql" not in feature.tags:
        singleton_instances.clear()
        clean_browser(context)


def before_scenario(context, scenario):
    context.logger.info(f"Running Scenario: {scenario.name}")


def after_scenario(context, scenario):
    if scenario.status == Status.failed:
        if "graphql" not in context.feature.tags:
            allure.attach(context.driver.get_screenshot_as_png(), name=f'screenshot-{scenario.name}',
                          attachment_type=allure.attachment_type.PNG)

    if "clear_cart" in scenario.tags:
        execute_gql(context, EMPTY_CART, do_assert=False)
