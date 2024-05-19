import requests

def evernote(email):

    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en,en-US;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.evernote.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://www.evernote.com/Login.action',
        'TE': 'Trailers',
    }
    data = requests.get("https://www.evernote.com/Login.action", headers=headers)
    data2 = {
        'username': email,
        'evaluateUsername': '',
        'hpts': data.text.split('document.getElementById("hpts").value = "')[1].split('"')[0],
        'hptsh': data.text.split('document.getElementById("hptsh").value = "')[1].split('"')[0],
        'analyticsLoginOrigin': 'login_action',
        'clipperFlow': 'false',
        'showSwitchService': 'true',
        'usernameImmutable': 'false',
        '_sourcePage': data.text.split('<input type="hidden" name="_sourcePage" value="')[1].split('"')[0],
        '__fp': data.text.split('<input type="hidden" name="__fp" value="')[1].split('"')[0]
    }
    response = requests.post('https://www.evernote.com/Login.action', data=data2, headers=headers)
    if "usePasswordAuth" in response.text:
        return True
    elif "displayMessage" in response.text:
        return False
    else:
        return False