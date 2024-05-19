# UserTrace

UserTrace is a Python script that allows you to search for a username across multiple sites. It retrieves information related to the provided username from various platforms and prints the results.

## Features
- Search for a username across supported sites.
- Retrieve and display information such as site name, category, and link for each result.
- Utilizes asynchronous HTTP requests for efficient scanning.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your_username/UserTrace.git
   ```
2. Navigate to the project directory:
   ```bash
   cd UserTrace
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script with the username you want to search for as an argument:
```bash
python script.py <username>
```
Replace `<username>` with the username you want to search for.

## Workflow Explanation

### JSON Structure

Here's the explanation added to the JSON data for the site looking for "Twitter archived profile":

```json
{
    "name": "Twitter archived profile",
    "uri_check": "http://archive.org/wayback/available?url=https://twitter.com/{account}",
    "uri_pretty": "https://web.archive.org/web/2/https://twitter.com/{account}",
    "e_code": 200,
    "e_string": "\"archived_snapshots\": {\"closest\"",
    "m_string": "\"archived_snapshots\": {}",
    "m_code": 200,
    "known": ["jack", "dineshdsouza"],
    "cat": "archived"
}
```

### Code Structure
The script is structured into several functions:

1. `read_json()`: Reads data from 'data.json' file.
2. `SuppressedStderr`: A context manager class to suppress specific warning messages.
3. `print_data_with_color(data)`: Prints data with colors.
4. `scan_site(session, site, username)`: Asynchronously scans a single site for the target username.
5. `scan_for_username(username)`: Asynchronously scans all supported sites for the target username.
6. `get_user_info(username)`: Asynchronously gets JSON data for a given username.
7. `whatsmyname_search(username)`: Calls `get_user_info(username)` function.
8. `main()`: Entry point of the script.



Explanation:
- `"name"`: Specifies the name of the site, which is "Twitter archived profile".
- `"uri_check"`: Provides the URI used to check if the Twitter profile is archived on the Wayback Machine. The `{account}` placeholder will be replaced with the username during runtime.
- `"uri_pretty"`: Offers a more readable URI for accessing the archived Twitter profile directly from the Wayback Machine.
- `"e_code"`: Represents the expected HTTP status code indicating a successful response when checking for the archived profile.
- `"e_string"`: Indicates the expected string in the response that signifies the profile is archived. If this string is found, it confirms that the profile is archived.
- `"m_string"`: Specifies a string in the response that indicates the profile is not archived. If this string is found, it implies that the profile is not archived.
- `"m_code"`: Represents the HTTP status code indicating a successful response when the profile is not archived.
- `"known"`: Lists known usernames associated with this site.
- `"cat"`: Defines the category of the site, which is "archived" in this case.


```python
if site["e_string"] in text:
    # If the expected string (e_string) is found in the response text,
    # it indicates that the username exists on the site.
    # Therefore, we extract relevant data and store it in the 'data' dictionary.
    data = {
        "Site": site["name"],    # Store the site name.
        "Category": cat,         # Store the category of the site.
        "Link": uri_check       # Store the link where the username was found.
    }
```

Explanation:
- The variable `site["e_string"]` represents an expected string that is expected to exist in the response text from the site if the username is found.
- The condition `if site["e_string"] in text:` checks if this expected string is present in the text obtained from the site's response.
- If the expected string is found in the response text, it confirms the existence of the username on the site.
- In such a case, relevant data including the site name, category, and link where the username was found are extracted and stored in the `data` dictionary.
- This data is later used to print the information about the site where the username was found.

### Scanning Workflow
- The `main()` function initializes the script and displays a banner.
- The script then searches for the provided username using `whatsmyname_search(username)` function.
- Inside `whatsmyname_search(username)` function, `get_user_info(username)` is called.
- `get_user_info(username)` initiates the asynchronous scanning process using `scan_for_username(username)`.
- `scan_for_username(username)` reads data from 'data.json' and asynchronously scans each supported site for the target username.
- For each site, the function `scan_site(session, site, username)` is called.
- Inside `scan_site(session, site, username)`, an asynchronous HTTP request is made to the URI constructed for the given site.
- If the username is found on the site, relevant data is extracted and printed using `print_data_with_color(data)` function.

## Contributing
Contributions are welcome! If you have any ideas, enhancements, or bug fixes, feel free to open an issue or create a pull request.

## Sample Output
```--------------------------------------------------
Site: Wikidot
Category: social
Link: http://www.wikidot.com/user:info/john
--------------------------------------------------
Site: discuss.elastic.co
Category: tech
Link: https://discuss.elastic.co/u/john
--------------------------------------------------
Site: untappd
Category: social
Link: https://untappd.com/user/john/
--------------------------------------------------
Site: Sourceforge
Category: coding
Link: https://sourceforge.net/u/john/profile
```