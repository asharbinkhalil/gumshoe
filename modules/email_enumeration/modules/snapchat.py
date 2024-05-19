import aiohttp
import asyncio
import json

async def snapchat_email(email):
    headers = {
        'Content-Type': 'text/plain',
    }

    data = {'email': email}

    async with aiohttp.ClientSession() as session:
        async with session.post('https://bitmoji.api.snapchat.com/api/user/find', headers=headers, data=json.dumps(data)) as response:
            checker = await response.text()

    text = '{"account_type":"snapchat"}'

    if text in checker:
        print("There Exist a Snapchat account with the email")
        return  True
    else:
        return False
