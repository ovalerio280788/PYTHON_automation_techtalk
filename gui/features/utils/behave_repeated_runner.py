import functools

from behave.model import ScenarioOutline


def patch_scenario_with_repeat(scenario, logger, max_repeat=1):
    """Monkey-patches :func:`~behave.model.Scenario.run()` to repeat a
    scenario more than one time base on a flag. The scenario is repeated a number of times
    to allow programmers to run a test many times and try to avoid sending flaky tests to
    develop and/or master branches.
    :param scenario:      Scenario or ScenarioOutline to patch.
    :param logger:        Logger instance to allow to print pretty messages/logs.
    :param max_repeat:    How many times the scenario can be run.
    """

    def scenario_run_with_repeat(scenario_name, *args, **kwargs):
        for attempt in range(1, max_repeat + 1):
            logger.info(f"RUNNING SCENARIO '{scenario_name}' REPEATED. COUNT #{attempt} out of {max_repeat}.")
            attempt += 1
            if not scenario_run(*args, **kwargs):
                if attempt < max_repeat + 1:
                    continue
        return True

    if isinstance(scenario, ScenarioOutline):
        scenario_outline = scenario
        for scenario in scenario_outline.scenarios:
            scenario_run = scenario.run
            scenario.run = functools.partial(scenario_run_with_repeat, scenario.name)
    else:
        scenario_run = scenario.run
        scenario.run = functools.partial(scenario_run_with_repeat, scenario.name)
