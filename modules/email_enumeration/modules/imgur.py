import aiohttp
import asyncio

async def imgur_email(email):
    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    data = 'email={}'.format(email)

    async with aiohttp.ClientSession() as session:
        async with session.post('https://imgur.com/signin/ajax_email_available', headers=headers, data=data) as response:
            checker = await response.text()

    text = '{"data":{"available":false},"success":true,"status":200}'

    if text in checker:
        print("Found an Imgur account with the email")
        return True
    else:
        return False

