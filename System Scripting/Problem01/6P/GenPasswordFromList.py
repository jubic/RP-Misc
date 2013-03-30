import random

password_list = ["p9otof", "ded82do", "deadbeef", "Dce872dt", "frKteV8"]

# Generate a random number fro 0 to length of list above - 1 (4)
# this will be the random index
pick = random.randint(0, len(password_list) - 1)

# use that random index to select a password from password_list
print password_list[pick]
