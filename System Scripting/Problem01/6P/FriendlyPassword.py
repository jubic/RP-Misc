import random
import string

letters = string.letters # a to z, A to Z
numbers = string.digits  # 0 to 9
MAXLENGTH = 10

friendly = ["Java", "Python", "Sydney", "Spain", "Gorilla", 
		"Pizza", "Coffee", "Train", "Apple", "Joker"]

def gen_password():
	# generate random number from 0 to 9 (friendly list has length 
	# of 9
	pick = random.randint(0, len(friendly) - 1)	
	# Use the random number above to pick password from the list
	password = friendly[pick]

	# MAXLENGTH - length of above word = random letter and digit to add
	letters_to_add = MAXLENGTH - len(password)

	# generate the remaining letters
	# leave 1 character out to add a digit later
	for i in range(letters_to_add - 1):
		pick = random.randint(0, len(letters) - 1)
		password += letters[pick]
	
	# generate a random index to pick on a digit
	pick = random.randint(0, len(numbers) - 1)
	password += numbers[pick]

	return password


for i in range(10):
	print gen_password()
	
