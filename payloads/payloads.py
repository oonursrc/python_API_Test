import pytest

def check_QueryInfoResponse(payload,username):

    print("Name: "+ payload["name"] + " , UserName: "+ payload["username"])

    name=username+"name"
    uname=username+"username"

    if payload["name"]==pytest.config['PAYLOAD_ELEMENTS'][name] and payload["username"]==pytest.config['PAYLOAD_ELEMENTS'][uname]:
        return True
    else: return False


def check_QueryInfoResponse_forNonexistingUser(payload,username):

    if payload["status"]==int(pytest.config['STATUS_CODES']['NotFound']) and payload["message"]=="Username "+username+" does not exist.":
        return True
    else: return False




def create_signup_payload():
    pass

def create_deleteuser_payload(pload):
    p_dict="{" \
           "\"id\":\""+str(pload['id'])+"\"," \
           "\"name\":\""+str(pload['name'])+"\"," \
           "\"username\":\""+str(pload['username'])+"\"," \
           "\"email\":\""+str(pload['email'])+"\"," \
           "\"superpower\":\""+str(pload['superpower'])+"\"," \
           "\"dateOfBirth\":\""+str(pload['dateOfBirth'])+"\"," \
           "\"isAdmin\":\""+str(pload['isAdmin']).lower()+"\"" \
           "}"

    return  p_dict