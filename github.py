import requests, json, os
from colorama import Fore, Style

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

class color:
    RED = Fore.RED + Style.BRIGHT
    RESET = Fore.RESET + Style.RESET_ALL
    WHITE = Fore.WHITE + Style.BRIGHT

def error(text):
    print(color.RED + '\n  [-] Inecpected error in the tool: ' + color.WHITE + str(text))
    choice = input(color.RED + '  [+] Press ENTER to return the menu: ')
    main()

def ret():
    choice = input(color.RED + '\n  [+] Press ENTER to return the menu: ')
    main()

def github_lookup(github_username):
    try:
        req = requests.get(f"https://api.github.com/users/{github_username}")
        req.raise_for_status() 
        res = json.loads(req.text)

        print(color.RED + '\n  GitHub user information')
        print(color.RED + '  ' + '=' * 70)
        for key, value in res.items():
            print(color.WHITE + f"  {key}: {value}")

        print(color.RED + '  ' + '=' * 70)


    except requests.exceptions.HTTPError as http_err: error(http_err)
    except requests.exceptions.RequestException as err: error(err)
    except json.JSONDecodeError: error('Error decoding JSON response')
    except Exception as e: error(e)

    ret()

def main():
    clear()
    title = '''
   ██████╗ ██╗████████╗██╗  ██╗██╗   ██╗██████╗ 
  ██╔════╝ ██║╚══██╔══╝██║  ██║██║   ██║██╔══██╗
  ██║  ███╗██║   ██║   ███████║██║   ██║██████╔╝
  ██║   ██║██║   ██║   ██╔══██║██║   ██║██╔══██╗
  ╚██████╔╝██║   ██║   ██║  ██║╚██████╔╝██████╔╝
   ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝
     [ GitHub lookup tool by Free for REAL ]
'''
    print(color.RED + title)
    choice = input(color.WHITE + '  [+] Enter the GitHub username: ')
    github_lookup(choice)

if __name__ == "__main__":
    try: main()
    except: error('Error launching the tool')