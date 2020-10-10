# coding=utf-8
"""QueryUserInformation feature steps."""

from utilities.request import *
from utilities.getset_instance import *

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)



@scenario('../../features/SignUp/signup.feature', 'Verify signup API functionality')
def test_verify_signup_api_functionality():
    """Verify signup API functionality."""

@given('SignUp is going to be executed')
def signup_is_going_to_be_executed():
    """SignUp is going to be executed."""
    logger.info("SignUp API will be executed")

@when('SignUp API executed with for a new user with <info_dict> infos')
def signup_api_executed_with_for_a_new_user_with_info_dict_infos(info_dict):
    """SignUp API executed with for a new user with <info_dict> infos."""
    signup_a_user(info_dict)

@then('Signup and query operation for <username> is successful')
def signup_and_query_operation_for_username_is_successful(username):
    """Signup and query operation for <username> is successful."""
    query_one_user("username",username)
    if (get_status_instance()==int(pytest.config['STATUS_CODES']['OK'])):
        ret=check_QueryInfoResponse(get_payload_instance(),username)
        assert ret==True,logger.error(pytest.config['RESPONSE_MSG']['NewUserCantFound'])
    else:
        logger.error("User with username "+username+" cannot be found")

