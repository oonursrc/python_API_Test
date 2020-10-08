# coding=utf-8
"""QueryUserInformation feature steps."""


from utilities.request import *
from utilities.getset_instance import *
from apiObjects.Status import *


from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

@scenario('../../features/QueryUserInformation/getuserinformation.feature', 'Verify user information query API functionality')
def test_verify_user_information_query_api_functionality():
    """Verify user information query API functionality."""

@scenario('../../features/QueryUserInformation/getuserinformation.feature', 'Verify user information query API functionality if user not exist')
def test_verify_user_information_query_api_functionality_if_user_not_exist():
    """Verify user information query API functionality if user not exist."""

@scenario('../../features/QueryUserInformation/getuserinformation.feature', 'Verify user information query API functionality with wrong query parameter')
def test_verify_user_information_query_api_functionality_with_wrong_query_parameter():
    """Verify user information query API functionality with wrong query parameter."""


@given('Query User Information is going to be executed')
def query_user_information_is_going_to_be_executed():
    """Username admin is provided to API."""
    logger.info("QueryUserInformation API will be executed")

@when('Query User Information API executed with <username>')
def query_user_information_api_executed_with_username(username):
    """QueryUserInformation API executed."""
    req=query_one_user("username",username)
    print("Resp Status Code: "+str(req.status_code))
    if(get_status_instance()==int(pytest.config['STATUS_CODES']['NotFound'])):logger.error(username+" "+pytest.config['RESPONSE_MSG']['UserCantFound'])
    set_status_instance(req.status_code)
    #res_status.set_instance(req.status_code)

@when('Query User Information API executed for nonexising user <username>')
def query_user_information_api_executed_for_nonexising_user(username):
    """QueryUserInformation API executed."""
    req = query_one_user("username",username)
    print("Resp Status Code: " + str(req.status_code))
    set_status_instance(req.status_code)

@when('Query User Information API executed for <username> with wrong query parameter')
def query_user_information_api_executed_for_username_with_wrong_query_parameter(username):
    """Query User Information API executed for <username> with wrong query parameter."""
    req = query_one_user("nokey", username)
    print("Resp Status Code: " + str(req.status_code))
    set_status_instance(req.status_code)

@then('Query operation for <username> is successful')
def query_operation_for_username_is_successful(username):
    """Query operation is successful."""
    #global res_status
    logger.info("Response code control for QueryUserInformation API")
    assert get_status_instance()==int(pytest.config['STATUS_CODES']['OK']),logger.error(pytest.config['RESPONSE_MSG']['QueryUserInforFailed'])
    logger.info("QueryUserInformation API successful")
    ret=check_QueryInfoResponse(get_payload_instance(),username)
    assert ret==True,logger.error(pytest.config['RESPONSE_MSG']['UserCantFound'])


@then('Query operation for <username> returns 404')
def query_operation_for_username_returns_404(username):
    """Query operation is successful."""
    ret=check_QueryInfoResponse_forNonexistingUser(get_payload_instance(),username)
    assert ret == True, logger.error("Query fail for nonexisting user")


@then('Query operation for <username> returns 400')
def query_operation_for_username_returns_400(username):
    """Query operation for <username> returns 400."""
    assert get_status_instance() == int(pytest.config['STATUS_CODES']['BadRequest']), logger.error(pytest.config['RESPONSE_MSG']['QueryUserInforFailed'])
