import requests

def hubspot(email):

    headers = {
                'User-Agent': "Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        'content-type': 'application/json',
        'origin': 'https://app.hubspot.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://app.hubspot.com/',
        'accept-language': 'en-US;q=0.8,en;q=0.7',
    }

    data = '{"email":"' + email + '","password":"","rememberLogin":false}'

    response = requests.post('https://api.hubspot.com/login-api/v1/login', headers=headers, data=data)

    if response.status_code == 400:
        if response.json()["status"] == "INVALID_PASSWORD":
            return True
        elif response.json()["status"] == "INVALID_USER":
            return False

    return False
