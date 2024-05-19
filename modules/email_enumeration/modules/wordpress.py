import aiohttp
import asyncio

async def wordpress_email(email):
    params = {'http_envelope': '1'}

    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://public-api.wordpress.com/rest/v1.1/users/{email}/auth-options', params=params) as response:
            checker = await response.text()

    text = '"email_verified": true'

    if text in checker:
        print("There Exist a WordPress account with the email")
        return True
    else:
        return False

