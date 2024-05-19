import aiohttp
import asyncio
import hashlib
import json

async def hash_email(email):
    md5_hash = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    url = f'https://en.gravatar.com/{md5_hash}.json'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def gravatar_email(email):
    md5_hash = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    url = f'https://en.gravatar.com/{md5_hash}.json'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            checker = await response.text()

    text = '"User not found"'

    if text in checker:
        return False
    else:
        print("There Exist a Gravatar account with the email")
        return True

async def parse_json(json_response, field):
    # Check if the input is a non-empty string and parse it
    if isinstance(json_response, str) and json_response.strip():
        try:
            json_response = json.loads(json_response)
        except json.JSONDecodeError:
            return None

    try:
        entry = json_response["entry"][0]
        return entry[field] if field in entry else None
    except (KeyError, IndexError):
        return None

