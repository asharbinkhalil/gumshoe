import requests


def eventbrite(email):
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        'Accept': '*/*',
        'Accept-Language': 'en,en-US;q=0.5',
        'Referer': 'https://www.eventbrite.com/',
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.eventbrite.com',
        'DNT': '1',
        'Connection': 'keep-alive',
    }

    try:
        req = requests.get("https://www.eventbrite.com/signin/?referrer=%2F", headers=headers)
        csrf_token = req.cookies["csrftoken"]

    except Exception:
        return False

    cookies = {  'csrftoken': csrf_token,  }

    headers["X-CSRFToken"] = csrf_token
    data = '{"email":"' + email + '"}'

    response = requests.post(
        'https://www.eventbrite.com/api/v3/users/lookup/',
        headers=headers,
        cookies=cookies,
        data=data)
    if response.status_code == 200:
        try:
            reqd = response.json()
            if reqd["exists"]:
                return True
            else:
                return False
        except Exception:
            return False
    else:
        return False