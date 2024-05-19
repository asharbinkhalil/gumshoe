import aiohttp
from apikeys import github_api_key

headers = {
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
    'Authorization': 'Bearer '+github_api_key, # Add your API token here
}

async def github_email(email):
    params = {
        'q': email,
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get('https://api.github.com/search/users', params=params) as response:
            json_response = await response.json()
    try:
        if  json_response["total_count"] == 0:
            return False
    except:
        pass
    else:
        print("There Exist a GitHub account with the email")
        return True

async def get_username(email):
    params = {
        'q': email,
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get('https://api.github.com/search/users', params=params) as response:
            json_response = await response.json()

    username = json_response["items"][0]["login"]
    return username

async def githubname_email(email):
    params = {
        'q': email,
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get('https://api.github.com/search/users', params=params) as response:
            json_response = await response.json()

    try:
        login = json_response["items"][0]["login"]
    except:
        return 'N/A'

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(f'https://api.github.com/users/{login}') as response:
            json_response = await response.json()

    name = json_response.get("name", 'N/A')
    return name

async def githublocation_email(email):
    params = {
        'q': email,
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get('https://api.github.com/search/users', params=params) as response:
            json_response = await response.json()

    try:
        items = json_response["items"]
    except KeyError:
        return 'N/A'

    if not items:  # Check if items is empty
        return 'N/A'

    login = items[0]["login"]

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(f'https://api.github.com/users/{login}') as response:
            json_response = await response.json()

    location = json_response.get("location", 'N/A')
    return location

async def github_avatar_url(email):
    params = {
        'q': email,
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get('https://api.github.com/search/users', params=params) as response:
            json_response = await response.json()
    try:
        items = json_response["items"]
    except KeyError:
        return 'N/A'
    try:
        login = json_response["items"][0]["login"]
    except IndexError:
        return 'N/A'

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(f'https://api.github.com/users/{login}') as response:
            json_response = await response.json()

    avatar_url = json_response.get("avatar_url", 'N/A')
    return avatar_url

