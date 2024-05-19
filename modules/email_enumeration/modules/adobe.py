import aiohttp

async def adobe_email(email):
    headers = {
        'content-type': 'application/json',
        'x-ims-clientid': 'adobedotcom2',
    }

    json_data = {
        'username': email,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post('https://auth.services.adobe.com/signin/v2/users/accounts',
                                headers=headers,
                                json=json_data) as response:
            checker = await response.text()

    adobe = '"type"'
    if adobe in checker:
        return True
    else:
        return False

async def adobe_facebook_email(email):
    headers = {
        'content-type': 'application/json',
        'x-ims-clientid': 'adobedotcom2',
    }

    json_data = {
        'username': email,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post('https://auth.services.adobe.com/signin/v2/users/accounts',
                                headers=headers,
                                json=json_data) as response:
            html = await response.text()

    facebook = 'facebook'
    if facebook in html:
        print("There Exist a adobe account with the email")
        return True
    else:
        return False

async def adobe_image(email):
    headers = {
        'content-type': 'application/json',
        'x-ims-clientid': 'adobedotcom2',
    }

    json_data = {
        'username': email,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post('https://auth.services.adobe.com/signin/v2/users/accounts',
                                headers=headers,
                                json=json_data) as response:
            data = await response.json()

    try:
        image_url = data[0]['images']['230']
    except:
        return 'N/A'

    if image_url:
        return image_url
    else:
        return 'N/A'