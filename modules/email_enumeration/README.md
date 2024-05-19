# Email Enumeration

The **Email Enumeration** project is a tool designed for discovering information associated with a given email address across various online platforms. It provides a comprehensive analysis of the email address, including its presence on social media, forums, and other websites, as well as potential security risks associated with it.

## Modules

The project comprises several modules, each responsible for checking the email address against different online platforms and services. Here's a brief overview of each module:

1. **Twitter**: Checks if the email is associated with a Twitter account.
2. **Snapchat**: Checks if the email is linked to a Snapchat account.
3. **MeWe**: Verifies the existence of a MeWe account with the email.
4. **Verify**: Performs basic email verification checks (e.g., syntax, domain existence).
5. **Duolingo**: Checks if the email is registered on Duolingo and retrieves associated details.
6. **Adobe**: Verifies Adobe accounts and retrieves additional information if available.
7. **WordPress**: Checks if the email is linked to a WordPress account.
8. **Imgur**: Verifies Imgur accounts associated with the email.
9. **Hulu**: Checks for Hulu accounts registered with the email.
10. **Rubmaps**: Verifies if the email is associated with a Rubmaps account.
11. **GitHub**: Checks GitHub for accounts associated with the email and retrieves user details.
12. **Gravatar**: Checks for Gravatar accounts linked to the email and fetches associated data.
13. **Discord**: Verifies the presence of a Discord account with the email.
14. **Spotify**: Checks if the email is used for a Spotify account.
15. **LeakCheck**: Scans known data breaches to determine if the email has been compromised.

## Strategy

The tool follows a strategy of asynchronous email checking to ensure efficient and timely retrieval of information from various platforms. It utilizes asynchronous programming with `asyncio` and `aiohttp` to perform concurrent requests, minimizing the overall execution time.

The process involves sending requests to the respective platform's endpoints or APIs, parsing the responses, and extracting relevant information. Each module employs different techniques tailored to the platform it targets, such as checking API endpoints, parsing HTML responses, or utilizing third-party APIs for additional data.

## How to Use

To utilize the Email Enumeration tool:

1. Ensure you have the necessary Python dependencies installed. You can install them using `pip`.
2. Import the required modules from the `email_enumeration.modules` package.
3. Call the `email_search(email)` function, passing the email address you want to investigate as an argument.
4. The tool will asynchronously check the email across multiple platforms and provide a detailed report containing information retrieved from each module.

## Example

```python
from email_enumeration import email_search

# Specify the email address to investigate
email = "example@example.com"

# Run the email search
email_search(email)
```

## Disclaimer

The Email Enumeration tool is designed for informational purposes only. It should be used responsibly and ethically, respecting the privacy and terms of service of the targeted platforms. The tool's results may not always be accurate or up-to-date, and it should not be used for illegal or malicious activities.