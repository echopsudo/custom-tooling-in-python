import sys
import requests
import re

print("Custom Tooling: Python Directory \n")

def help():
    print("Help for this script")
    print("Usage: python3 enum.py 127.0.0.1 wordlist_file.txt")

def dir():
    try:
        if len(sys.argv) == 3:
            ip_regex = r"^([0-9]{1,3}\.){3}[0-9]{1,3}$"
            if re.match(ip_regex, sys.argv[1]):
                ip = sys.argv[1]
                wordlist_file = open(f"{sys.argv[2]}", "r")
            else:
                ip = sys.argv[2]
                wordlist_file = open(f"{sys.argv[1]}", "r")
            wordlist = wordlist_file.read().splitlines()
        else:
            print("It looks like you didn't provide any arguments")
            ip = input("Please enter the IP you want to enumerate: ")
            wordlist_path = input("Please enter the wordlist file: ")
            wordlist_file = open(f"{wordlist_path}", "r")
            wordlist = wordlist_file.read().splitlines()
    except:
        print("Wordlist not found!")
        sys.exit()

    print("Running directory enumeration!\n")

    try:
        for words in wordlist:
            site = f"http://{ip}/{words}"
            response = requests.get(site)
            codes = response.status_code
            if codes == 404:
                pass
            else:
                print(f"{site}: {codes}")
    except:
        print("IP or Port is not opened!")
        sys.exit()


#make a mode to enumerate subdomains later
mode = input("do you want to enumerate dir/sub: ")

while True:
    if mode == "dir":
        dir()
    #elif mode == "sub":
        #sub()
    elif mode == "--help":
        help()
    else:
        print("invalid choice, see --help")
