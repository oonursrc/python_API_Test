import pytest
import requests
from payloads.payloads import *
from payloads.Payload import *
from apiObjects.Status import *
from loguru import logger

from utilities.getset_instance import *


def query_one_user(key,username): #get request

    url=pytest.config['URL']['UserInformation']
    req = requests.get(url+ key + "=" + username)
    print("QueryUserInformation API: "+req.text)
    try:
        set_payload_instance(req.json())
        #payload.set_instance(req.json())
    except Exception:
        print("QueryUserInformation API response is not json")
    return req

def signup_a_user(info_dict): #post request
    header = {'Content-Type': 'application/json'}
    url = pytest.config['URL']['SignUp']
    req = requests.post(url, headers=header, data=info_dict)
    set_status_instance(req.status_code)
    #res_status.set_instance(req.status_code)
    print("SignUp API: " + req.text)
    logger.info("Response code control for SignUp API")
    assert get_status_instance() == int(pytest.config['STATUS_CODES']['Created']), logger.error(
        pytest.config['RESPONSE_MSG']['SignUpFailed'])
    logger.info("SignUp API successful")

def delete_user(): #delete request

    delete_req_payload=create_deleteuser_payload(get_payload_instance())

    print("Delete Query Payload: "+delete_req_payload)

    url = pytest.config['URL']['Delete']
    header = {'Content-Type': 'application/json'}
    req = requests.delete(url, data=delete_req_payload, headers=header, auth=(pytest.config['AUTH']['testername'], pytest.config['AUTH']['testerpassword']))
    print("Delete API: " + req.text)