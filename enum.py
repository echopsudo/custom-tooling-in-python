import sys
import requests
import re


print("Custom Tooling: Python Directory \n")


def help():
    print("Help for this script")
    print("Usage: python3 enum.py 127.0.0.1 wordlist_file.txt")


def enumerate_dir():
    try:
        if len(sys.argv) == 3:
            ip_regex = r"^([0-9]{1,3}\.){3}[0-9]{1,3}$"
            if re.match(ip_regex, sys.argv[1]):
                ip = sys.argv[1]
                with open(f"{sys.argv[2]}", "r") as wordlist_file:
                    wordlist = wordlist_file.read().splitlines()
            else:
                ip = sys.argv[2]
                with open(f"{sys.argv[1]}", "r") as wordlist_file:
                    wordlist = wordlist_file.read().splitlines()
        else:
                print("It looks like you didn't provide any arguments")
                ip = input("Please enter the IP you want to enumerate: ")
                wordlist_path = input("Please enter the wordlist file: ")
                with open(f"{wordlist_path}", "r") as wordlist_file:
                    wordlist = wordlist_file.read().splitlines()
    except FileNotFoundError:
        print("Wordlist not found!")
        sys.exit()

    print("Running directory enumeration!\n")

    try:
        for words in wordlist:
            site = f"http://{ip}/{words}"
            response = requests.get(site, timeout=3)
            codes = response.status_code
            if codes == 404:
                pass
            else:
                print(f"{site}: {codes}")
    except requests.exceptions.RequestException:
        print("IP or Port is not opened!")
        sys.exit()


# make a mode to enumerate subdomains later
mode = input("do you want to enumerate dir/sub: ")


if mode == "dir":
    enumerate_dir()
# elif mode == "sub":
    # sub()
elif mode == "--help":
    help()
else:
    print("invalid choice, see --help")
