import json
import aiohttp
import asyncio
import sys,os
import colorama
colorama.init()

# Read data from 'data.json'
def read_json():
    with open("modules/username_enumeration/data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return data

# Suppress specific warning messages from being displayed on the terminal
class SuppressedStderr:
    def __enter__(self):
        self._stderr = sys.stderr
        sys.stderr = open(os.devnull, 'w')  # Redirect stderr to os.devnull

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stderr.close()
        sys.stderr = self._stderr

# Function to print data with colors
def print_data_with_color(data):
    print(colorama.Fore.YELLOW + "Site: " + colorama.Fore.RESET + data["Site"]   , colorama.Fore.BLUE + "Category: " + colorama.Fore.RESET + data["Category"])
    print(colorama.Fore.GREEN + "Link: " + colorama.Fore.RESET + data["Link"])
    print("-" * 50)

# Function to scan a single site for the target username
async def scan_site(session, site, username):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36", 
  }
    uri_check = site["uri_check"].format(account=username)
    cat = site["cat"]
    try:
        async with session.get(uri_check, headers=headers, timeout=15, raise_for_status=False) as res:
            if res.status == 200:
                text = await res.text()
                if site["e_string"] in text:
                    data = {
                        "Site": site["name"],
                        "Category": cat,
                        "Link": uri_check
                    }
                    print_data_with_color(data)  # Print the data with colors if site is present
    except Exception as e:
        pass


# Function to scan all supported sites for the target username
async def scan_for_username(username):
    data = read_json()
    # Create a session for making asynchronous HTTP requests
    async with aiohttp.ClientSession() as session:
        tasks = []
        for site in data["sites"]:
            tasks.append(scan_site(session, site, username))

        # Wait for all tasks to finish
        await asyncio.gather(*tasks)

# Function to get JSON data for a given username
async def get_user_info(username):
    await scan_for_username(username)

def username_search(username):
    with SuppressedStderr():
        asyncio.run(get_user_info(username))