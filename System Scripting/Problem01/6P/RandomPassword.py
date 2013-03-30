import random
import string

letters = string.letters # letters = a to z, A to Z
numbers = string.digits  # numbers = 0 to 9

def gen_password(length, number_length=1):
	# calculate how many letters should be generated
	letters_length = length - number_length

	# starts with a blank password
	password = ""

	# generate the letters
	for i in range(letters_length):
		pick = random.randint(0, len(letters) - 1)
		password += letters[pick]
	
	# generate the digits
	for i in range(number_length):
		pick = random.randint(0, len(numbers) - 1)
		password += numbers[pick]
	
	return password

for i in range(10):
	print gen_password(6, 2)

for i in range(10):
	print gen_password(8, 3)

for i in range(10):
	print gen_password(10, 4)
	
