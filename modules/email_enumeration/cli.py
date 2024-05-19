import asyncio
from modules.email_enumeration.modules.twitter import twitter_email
from modules.email_enumeration.modules.snapchat import snapchat_email
from modules.email_enumeration.modules.mewe import mewe_email
from modules.email_enumeration.modules.verify import *
from modules.email_enumeration.modules.duolingo import duolingo_name_check, duolingo_email, duolingo_image
from modules.email_enumeration.modules.adobe import adobe_email, adobe_facebook_email, adobe_image
from modules.email_enumeration.modules.wordpress import wordpress_email
from modules.email_enumeration.modules.imgur import imgur_email
from modules.email_enumeration.modules.hulu import hulu_email
from modules.email_enumeration.modules.rubmaps import rubmaps_email
from modules.email_enumeration.modules.github import *
from modules.email_enumeration.modules.gravatar import *
from modules.email_enumeration.modules.discord import *
from modules.email_enumeration.modules.spotify import spotify
# from modules.email_enumeration.modules.leakcheck import leakcheck
from modules.email_enumeration.modules.eventbrite import eventbrite
from modules.email_enumeration.modules.pinterest import pinterest
from modules.email_enumeration.modules.evernote import evernote
from modules.email_enumeration.modules.anydo import anydo
from modules.email_enumeration.modules.freelancer import freelancer
from modules.email_enumeration.modules.venmo import venmo
from modules.email_enumeration.modules.strava import strava
from modules.email_enumeration.modules.firefox import firefox
from modules.email_enumeration.modules.hubspot import hubspot
from modules.email_enumeration.modules.archive import archive
from modules.email_enumeration.modules.instagram import instagram




from rich import print as rich_print
from rich.console import Console



# Initialize rich console
console = Console()

# Function to print JSON with colors
def print_colored(json_data, indent=0):
    for key, value in json_data.items():
        if isinstance(value, dict):
            console.print(f"[yellow]{' ' * indent}{key}:")
            print_colored(value, indent + 2)
        elif isinstance(value, bool):
            
            if value:   
                rich_print(f"[green]{' ' * indent}{key}: {value}")
            else:
                console.print(f"[red]{' ' * indent}{key}: {value}")
        else:
            console.print(f"[reset]{' ' * indent}{key}: {value}")

async def check_email_async(email):
    twitter_result = await twitter_email(email)
    snapchat_result = await snapchat_email(email)
    mewe_result = await mewe_email(email)
    disposable_result = await disposable(email)
    spam_result = await spam(email)
    deliverable_result = await deliverable(email)
    duolingo_result = await duolingo_email(email)
    duolingo_name = await duolingo_name_check(email)
    duolingo_image_url = await duolingo_image(email)
    adobe_result = await adobe_email(email)
    adobe_image_url = await adobe_image(email)
    adobe_facebook_result = await adobe_facebook_email(email)
    wordpress_result = await wordpress_email(email)
    imgur_result = await imgur_email(email)
    hulu_result = await hulu_email(email)
    rubmaps_result = await rubmaps_email(email)
    github_result = await github_email(email)
    github_name = await githubname_email(email)
    github_location = await githublocation_email(email)
    github_image = await github_avatar_url(email)
    gravatar_response = await hash_email(email)
    gravatar_image = await parse_json(gravatar_response, 'thumbnailUrl')
    gravatar_result = await gravatar_email(email)
    discord_result = await discord_email(email)
    spotify_result = await spotify(email)
    # leakcheck_result=leakcheck(email)
    eventbrite_result =  eventbrite(email)
    pinterest_result =  pinterest(email)
    evernote_result =  evernote(email)
    anydo_result =  anydo(email)
    freelancer_result =  freelancer(email)
    venmo_result =  venmo(email)
    strava_result =  strava(email)
    firefox_result =  firefox(email)
    hubspot_result =  hubspot(email)
    archive_result =  archive(email)
    instagram_result = await instagram(email)

    

    # try:
    #     leakcheck_result['error']
    #     leakcheck_result = {"Congrats":"No Breaches Found!"}
    # except:
    #     pass
    result = {
        'Duolingo Name': duolingo_name,
        'GitHub Name': github_name,  
        'Location': github_location,  
        'Image': {
            'Duolingo': duolingo_image_url,
            'GitHub': github_image,
            'Gravatar': gravatar_image,
            'Adobe': adobe_image_url,
           
        },
        # 'LeakCheck': leakcheck_result,
        'Deliverable': deliverable_result,
        'Disposable': disposable_result,
        'Spam': spam_result,
       
        'Profiles':{
            'Facebook': adobe_facebook_result,
            'Twitter': twitter_result,
            'Snapchat': snapchat_result,
            'Github': github_result,
            'Gravatar': gravatar_result,
            'Discord': discord_result,
            'Spotify': spotify_result,
            'Adobe': adobe_result,
            'Wordpress': wordpress_result,
            'Duolingo': duolingo_result,
            'MeWe': mewe_result,
            'Imgur': imgur_result,
            'Hulu': hulu_result,
            'Rubmaps': rubmaps_result,
            'Eventbrite': eventbrite_result,
            'Pinterest': pinterest_result,
            'Evernote': evernote_result,
            'Anydo': anydo_result,
            'Freelancer': freelancer_result,
            'Venmo': venmo_result,
            'Strava': strava_result,
            'Firefox': firefox_result,
            'Hubspot': hubspot_result,
            'Archive': archive_result,
            "Instagram":instagram_result,

        },
    }

    return result

# Main function
async def check(email):
    result = await check_email_async(email)
    print_colored(result)


def email_search(email):
    asyncio.run(check(email))
