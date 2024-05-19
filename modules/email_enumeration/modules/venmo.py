import requests,json
def venmo(email):
        headers = {
            "Accept": "application/json",
            "Accept-Language": "en,en-US;q=0.5",
            "Referer": "https://venmo.com/",
            "Content-Type": "application/json",
            "Origin": "https://venmo.com",
            "DNT": "1",
            "Connection": "keep-alive",
            "TE": "Trailers",
        }
        requests.get("https://venmo.com/signup/email", headers=headers)
        data = str(
            json.dumps(
                {
                    "last_name": "Johnson",
                    "first_name": "James",
                    "email": str(email),
                    "password": "nicker1!",
                    "phone": "1234567890",
                    "client_id": 10,
                }
            )
        )

        response = requests.post(
            "https://venmo.com/api/v5/users", headers=headers, data=data
        )
        if "Not acceptable" not in response.text:
            if "That email is already registered in our system." in response.text:
                return True
            else:
                return False