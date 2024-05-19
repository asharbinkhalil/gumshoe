import aiohttp
import asyncio

async def deliverable(email):
    params = {'email': email}

    async with aiohttp.ClientSession() as session:
        async with session.get('http://api.eva.pingutil.com/email', params=params) as response:
            checker = await response.text()

    if '"deliverable":true' in checker:
        return 'true'
    else:
        return 'false'

async def spam(email):
    params = {'email': email}

    async with aiohttp.ClientSession() as session:
        async with session.get('http://api.eva.pingutil.com/email', params=params) as response:
            checker = await response.text()

    if '"spam":true' in checker:
        return 'true'
    else:
        return 'false'

async def disposable(email):
    params = {'email': email}

    async with aiohttp.ClientSession() as session:
        async with session.get('http://api.eva.pingutil.com/email', params=params) as response:
            checker = await response.text()

    if '"disposable":true' in checker:
        print("There Exist a disposable email")
        return True
    else:
        return False