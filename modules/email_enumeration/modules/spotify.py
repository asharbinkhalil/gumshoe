import aiohttp
import asyncio

async def spotify(email):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "DNT": "1",
        "Connection": "keep-alive",
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(
            "https://spclient.wg.spotify.com/signup/public/v1/account",
            params={"validate": "1", "email": str(email)}
        ) as response:
            resp = await response.json()

    if resp.get("status") == 20:
        print("There Exist a Spotify account with the email")
        return True
    
    return False

