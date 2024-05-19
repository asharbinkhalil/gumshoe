import requests
def freelancer(email):
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/json',
        'Origin': 'https://www.freelancer.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }
    data = '{"user":{"email":"' + email + '"}}'
    try:
        response = requests.post('https://www.freelancer.com/api/users/0.1/users/check?compact=true&new_errors=true', data=data, headers=headers)
        resData = response.json()
        if response.status_code == 409 and "EMAIL_ALREADY_IN_USE" in response.text:
            return True
        elif response.status_code == 200:
            return False
        else:
            return False
    except Exception:
        return False
    
