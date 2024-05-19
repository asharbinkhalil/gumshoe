import requests,json

def strava(email):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language": "en,en-US;q=0.5",
        "Referer": "https://www.strava.com/register/free?cta=sign-up&element=button&source=website_show",
        "DNT": "1",
        "Connection": "keep-alive",
        "TE": "Trailers",
    }

    r = requests.get(
        "https://www.strava.com/register/free?cta=sign-up&element=button&source=website_show",
        headers=headers,
    )
    try:
        headers["X-CSRF-Token"] = r.text.split('<meta name="csrf-token" content="')[
            1
        ].split('"')[0]
    except Exception:
        return False
    headers["X-Requested-With"] = "XMLHttpRequest"

    params = {"email": email}

    response = requests.get(
        "https://www.strava.com/athletes/email_unique", headers=headers, params=params
    )

    if response.text == "false":
        return True
    elif response.text == "true":
        return False
    else:
        return False
