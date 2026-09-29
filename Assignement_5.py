import re

s = input("Enter a string: ")

if re.fullmatch(r"[a-zA-Z0-9]+", s):
    print("String contains only a-z, A-Z and 0-9")
else:
    print("String contains other characters")
