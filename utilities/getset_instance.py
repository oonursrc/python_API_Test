
from payloads.Payload import *
from apiObjects.Status import *

res_status=Status().get_instance()
payload=Payload.get_instance()


def set_status_instance(status):
    res_status.set_instance(status)

def get_status_instance():
    return res_status.get_instance()

def set_payload_instance(req):
    payload.set_instance(req)

def get_payload_instance():
    return payload.get_instance()