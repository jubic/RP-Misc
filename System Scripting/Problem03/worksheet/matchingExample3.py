import re
# match a string contains character "4" to "7"
a = re.search("[4-7]", "It's 6PM")  # matched

print a