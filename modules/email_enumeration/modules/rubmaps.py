import aiohttp

async def rubmaps_email(email):
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }

    data = {
        'email': email,
        'ajax': '1',
    }

    async with aiohttp.ClientSession() as session:
        async with session.post('https://www.rubmaps.ch/signup', headers=headers, data=data) as response:
            checker = await response.text()
            if '0' in checker:
                return False
            else:
                print("There Exist a rubmaps account with the email")

                return True
