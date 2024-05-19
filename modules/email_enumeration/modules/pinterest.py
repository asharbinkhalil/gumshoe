import requests
def pinterest(email):
    req = requests.get(
        "https://www.pinterest.com/_ngjs/resource/EmailExistsResource/get/",
        params={
            "source_url": "/",
            "data": '{"options": {"email": "' + email + '"}, "context": {}}'})
    if 'source_field' in str(req.json()["resource_response"]["data"]) :
        return False

    elif req.json()["resource_response"]["data"]:
        return True
    else:
        return False