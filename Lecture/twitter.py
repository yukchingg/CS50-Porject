import re

url = input("URL: ").strip()

if matches := re.search("^(?:https?://)?(?:www\.)?twitter\.com/([A-Z0-9_]+)", url, re.IGNORECASE):
    print(f"Username: ",matches.group(1))