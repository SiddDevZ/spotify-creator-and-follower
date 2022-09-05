import os
try:
    import requests
    import colorama
except:
    os.system("pip3 install requests")
    os.system("pip3 install colorama")
    import requests
    import colorama
import random
from colorama import Fore
import threading
lock = threading.Lock()
def create():
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    email = ""
    password = ""
    for i in range(8):
        email = email + random.choice(a)
    email = email + "@gmail.com"
    for x in range(16):
        password = password + random.choice(a)
    try:
        headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://www.spotify.com/"
            }
        data = f"birth_day=1&birth_month=01&birth_year=1970&collect_personal_info=undefined&creation_flow=&creation_point=https://www.spotify.com/uk/&displayname=github.com/SiddDevZ&email={email}&gender=neutral&iagree=1&key=a1e486e2729f46d6bb368d6b2bcda326&password={password}&password_repeat={password}&platform=www&referrer=&send-email=1&thirdpartyemail=0&fb=0"
        req = requests.post(f"https://spclient.wg.spotify.com/signup/public/v1/account", headers=headers, data=data)
        if "login_token" in req.text:
            login_token = req.json()['login_token']
            with open("spotify.txt", "a") as f:
                f.write(f'{email}:{password}:{login_token}\n')
                return login_token
                
        else:
            print("error getting login_token")
            return None
    except:
        print("Error creating")
        
def get_csrf_token():
    try:
        r = requests.get("https://www.spotify.com/uk/signup/?forward_url=https://accounts.spotify.com/en/status&sp_t_counter=1")
        return r.text.split('csrfToken":"')[1].split('"')[0]
    except:
        return None, "error getting CSRF token"
def get_token(login_token):
        headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRF-Token": get_csrf_token(),
            "Host": "www.spotify.com"
        }
        requests.post("https://www.spotify.com/api/signup/authenticate", headers = headers, data = "splot=" + login_token)
        headers = {
            "accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "accept-language": "en",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "spotify-app-version": "1.1.52.204.ge43bc405",
            "app-platform": "WebPlayer",
            "Host": "open.spotify.com",
            "Referer": "https://open.spotify.com/"
        }
        try:
            r = requests.get(
                "https://open.spotify.com/get_access_token?reason=transport&productType=web_player",
                headers = headers
            )
            return r.json()["accessToken"]
        except:
            return None, "Error getting token"
def follow(profile):
    try:
            if "/user/" in profile:
                profile = profile.split("/user/")[1]
            if "?" in profile:
                profile = profile.split("?")[0]
            login_token = create()
            if login_token == None:
                print(f"{Fore.RED}while registering, ratelimit")
                return None
            auth_token = get_token(login_token=login_token)
            if auth_token == None:
                print(f"{Fore.RED}error while getting auth token")
                return None
            headers = {
                "accept": "application/json",
                "Accept-Encoding": "gzip, deflate, br",
                "accept-language": "en",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
                "app-platform": "WebPlayer",
                "Referer": "https://open.spotify.com/",
                "spotify-app-version": "1.1.52.204.ge43bc405",
                "authorization": "Bearer {}".format(auth_token),
            }
            requests.post("https://api.spotify.com/v1/me/following?type=user&ids=" + profile, headers = headers)
            print("Followed")
    except:
        print("Error while following")
print(f"""
{Fore.GREEN}  ██████  ██▓███   ▒█████  ▄▄▄█████▓ ██▓  █████▒▓██   ██▓
{Fore.GREEN}▒██    ▒ ▓██░  ██▒▒██▒  ██▒▓  ██▒ ▓▒▓██▒▓██   ▒  ▒██  ██▒
{Fore.GREEN}░ ▓██▄   ▓██░ ██▓▒▒██░  ██▒▒ ▓██░ ▒░▒██▒▒████ ░   ▒██ ██░
{Fore.GREEN}  ▒   ██▒▒██▄█▓▒ ▒▒██   ██░░ ▓██▓ ░ ░██░░▓█▒  ░   ░ ▐██▓░
{Fore.GREEN}▒██████▒▒▒██▒ ░  ░░ ████▓▒░  ▒██▒ ░ ░██░░▒█░      ░ ██▒▓░
{Fore.GREEN}▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▒░▒░   ▒ ░░   ░▓   ▒ ░       ██▒▒▒ 
{Fore.GREEN}░ ░▒  ░ ░░▒ ░       ░ ▒ ▒░     ░     ▒ ░ ░       ▓██ ░▒░ 
{Fore.GREEN}░  ░  ░  ░░       ░ ░ ░ ▒    ░       ▒ ░ ░ ░     ▒ ▒ ░░  
{Fore.GREEN}      ░               ░ ░            ░           ░ ░     
{Fore.GREEN}                                                 ░ ░           
                    {Fore.YELLOW}github.com/SiddDevZ
""")
print()
print("""
[+] Choose Option :-
    [1] Mass make spotify accounts
    [2] Make & Follow profile
    [3] Exit
          
""")
f = 0
op = int(input(">> "))
if op == 1:
    while True:
        threading.Thread(target = create).start()
elif op == 2:
    prof = str(input("enter profile link/name >> "))
    while True:
        threading.Thread(target = follow, args=(prof,)).start()
else:
    print("Exiting")
        