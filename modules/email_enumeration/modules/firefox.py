import requests

def firefox(email):

    url = "https://api.accounts.firefox.com/v1/account/status"
    data = {"email": email}

    req = requests.post(url, data=data)

    if "false" in req.text:
        return False
    elif "true" in req.text:
        return True
    else:
        return False