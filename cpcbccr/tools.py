import requests

def get(*args,**kwargs):
    return requests.get(*args,**kwargs)

def post(*args, **kwargs):
    return requests.post(*args, **kwargs)