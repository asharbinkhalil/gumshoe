import aiohttp
import asyncio,json

async def duolingo_name_check(email):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    params = {
        'email': email,
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get('https://www.duolingo.com/2017-06-30/users', params=params) as response:
            json_string = await response.text()

    data = json.loads(json_string)

    if len(data['users']) > 0:
        if 'name' in data['users'][0]:
            name = data['users'][0]['name']
            return name
        else:
            return 'N/A'
    else:
        return 'N/A'

async def duolingo_email(email):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    params = {
        'email': email,
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get('https://www.duolingo.com/2017-06-30/users', params=params) as response:
            checker = await response.text()

    text = 'username'

    if text in checker:
        print("There Exist a Duolingo account with the email")
        return True
    else:
        return False

async def duolingo_image(email):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    params = {
        'email': email,
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get('https://www.duolingo.com/2017-06-30/users', params=params) as response:
            json_string = await response.text()

    data = json.loads(json_string)

    if len(data['users']) > 0:
        if 'picture' in data['users'][0]:
            picture = data['users'][0]['picture']
            return picture
        else:
            return 'false'
    else:
        return 'false'

