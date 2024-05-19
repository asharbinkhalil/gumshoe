import sys
from modules.email_enumeration.cli import email_search
from modules.username_enumeration.script import username_search
from modules.suddomain_enumeration import domain_search

def print_banner():
    print("""
                            _                
                           | |               
   __ _ _   _ _ __ ___  ___| |__   ___   ___ 
  / _` | | | | '_ ` _ \/ __| '_ \ / _ \ / _ |
 | (_| | |_| | | | | | \__ \ | | | (_) |  __/
  \__, |\__,_|_| |_| |_|___/_| |_|\___/ \___|
   __/ |                                     
  |___/                                      

                                                    
    --------------------------------------
    |         Enumeration Script         |
    --------------------------------------
    | Options:                           |
    | 1. Search by Username              |
    | 2. Search by Email                 |
    | 3. Subdomain enumeration           |
    --------------------------------------
    """)

def main():
    print_banner()
    
    try:
        option = int(input("Enter your choice (1/2/3): "))
        
        if option == 1:
            username = input("Enter the username to search: ")
            username_search(username)
        elif option == 2:
            email = input("Enter the email to search: ")
            email_search(email)
        elif option == 3:
            domain = input("Enter the domain to search: ")
            domain_search(domain)
        else:
            print("Invalid option. Please choose a number from 1 to 3.")
            sys.exit(1)
            
    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit(1)

if __name__ == "__main__":
    main()
