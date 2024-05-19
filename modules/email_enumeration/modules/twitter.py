import aiohttp

async def twitter_email(email):
    async with aiohttp.ClientSession() as session:
        email_checker = f'https://api.x.com/i/users/email_available.json?email={email}'
        async with session.get(email_checker) as response:
            check = await response.json()
            if check["taken"]:
                print("There Exist a Twitter account with the email")
                return True
            else:
                return False
