import requests
from googlesearch import search
from urllib.parse import urlparse

# Function to get subdomains from Google
def get_subdomains_from_google(domain):
    google_query = f"site:*.{domain}"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
    urls_list = search(google_query, stop=5, user_agent=user_agent)
    subdomains_result = [urlparse(url).netloc for url in urls_list]
    subdomains_result = list(set(subdomains_result))  # Remove duplicated subdomains
    return subdomains_result


# Function to retrieve subdomains using crt.sh API
def get_subdomains(domain):
    subdomains = set()
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for entry in data:
                subdomain = entry['name_value']
                subdomains.add(subdomain)
    except Exception as e:
        print(f"Error fetching subdomains: {e}")
    return subdomains


# Function to print subdomains
def print_subdomains(subdomains):
    print(f"\nTotal subdomains found: {len(subdomains)}\n")
    for subdomain in subdomains:
        print(subdomain)

# # Main function
def domain_search(domain):
    import sys
# domain =sys.argv[1]
# print(f"\nScanning subdomains for: {domain}\n")
# subdomains = get_subdomains(domain)
# print_subdomains(subdomains)
# subdomains = get_subdomains_from_google(domain)
# print("Subdomains found:")
# for subdomain in subdomains:
#     print(subdomain)