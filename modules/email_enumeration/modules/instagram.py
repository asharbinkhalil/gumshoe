import aiohttp
async def instagram(email):
    url = "https://www.instagram.com/api/v1/public/landing_info/"
    endpoint = "https://www.instagram.com/accounts/web_create_ajax/attempt/"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            if "csrftoken" in r.cookies:
                token = r.cookies["csrftoken"].value
            else:
                raise ValueError("Token not found")

    async with aiohttp.ClientSession() as session:
        async with session.post(
            endpoint,
            data={"email": email},
            headers={"x-csrftoken": token}
        ) as r:
            json_body = await r.json()
            if json_body["status"] == "fail":
                return True
            if "email" not in json_body["errors"]:
                return False
            else:
                message = json_body["errors"]["email"][0]["message"]
                if json_body["errors"]["email"][0]["code"] == "email_is_taken":
                    return True
                if json_body["errors"]["email"][0]["code"] == "invalid_email":
                    return False
                else:
                    return False