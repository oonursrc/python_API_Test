import configparser
import pytest
import os
import sys
from loguru import logger
#sys.path.append('utilities')

@pytest.fixture(scope="session", autouse=True)
def get_config():
    pytest.root_dir = os.path.dirname(os.path.abspath(__file__))
    logger.info("Project root directory is : " + pytest.root_dir)
    pytest.config = configparser.ConfigParser()
    logger.info("Config directory is " + pytest.root_dir + '/utilities/properties.ini')
    pytest.config.read(pytest.root_dir + '/utilities/properties.ini')



def pytest_bdd_before_scenario(request, feature, scenario):
    """Called before scenario is executed."""
    print("----Scenario start----\n")


def pytest_bdd_after_scenario(request, feature, scenario):
    """Called after scenario is executed."""
    print("----Scenario end----\n")

def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    """Called before step function is set up."""


def pytest_bdd_before_step_call(request, feature, scenario, step, step_func, step_func_args):
    """Called before step function is executed."""


def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    """Called after step function is successfully executed."""


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    """Called when step function failed to execute."""


def pytest_bdd_step_validation_error(request, feature, scenario, step, step_func, step_func_args, exception):
    """Called when step failed to validate."""


def pytest_bdd_step_func_lookup_error(request, feature, scenario, step, exception):
    """Called when step lookup failed."""