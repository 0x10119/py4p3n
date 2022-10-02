import requests
import sys

subdomain = open("subdomain.txt").read()
subs = subdomain.splitlines()

for sub in subs:
    #print(sub)
    url_to_check = f"https://{sub}.{sys.argv[1]}"

    try:
        requests.get(url_to_check)
    except requests.ConnectionError:
        pass
    
    else:
        print("Valid domain: ", url_to_check)
    
    