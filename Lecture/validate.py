import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+.)?\w+.(edu|com)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invlid")
