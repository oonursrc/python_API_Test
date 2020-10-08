# coding=utf-8
"""SignUp feature tests."""


from utilities.request import *
from utilities.getset_instance import *
from steps.QueryUserInformation import test_query_user_information as queryuserinfo

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('../../features/DeleteUser/deleteuser.feature', 'Verify Delete API functionality')
def test_verify_delete_api_functionality():
    """Verify Delete API functionality."""


@given('Delete User API is going to be executed')
def delete_user_api_is_going_to_be_executed():
    """Delete User API is going to be executed."""
    logger.info("Delete USer API will be executed")


@when('Query User and Delete User API executed with for an existing user <username>')
def query_user_and_delete_user_api_executed_with_for_an_existing_user_username(username):
    """Query User and Delete User API executed with for an existing user <username>."""
    logger.info("Calling QueryUserInformation API executed with <username> step")
    queryuserinfo.query_user_information_api_executed_with_username(username)
    if(get_status_instance()==int(pytest.config['STATUS_CODES']['OK'])):
        delete_user()


@then('Delete User for <username> is successful')
def delete_user_for_username_is_successful():
    """Delete User for <username> is successful."""
    pass

