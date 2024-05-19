import aiohttp
import asyncio

async def mewe_email(email):
    headers = {
        'accept': 'application/json, text/plain, */*',
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://mewe.com/api/v2/auth/checkEmail?email={email}', headers=headers) as response:
            checker = await response.text()

    text = "Email already taken"

    if text in checker:
        print("There Exist a MeWe account with the email")
        return True
    else:
        return False