import random

letters = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z", "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

numbers = ("1","2","3","4","5","6","7","8","9","0")

def make_password(length, n):
	password = ""
	
	for i in range(length-n):
		letter = random.randint(0, 51)
		password = password + letters[letter] 
	
	for i in range(n):
		number = random.randint(0,9)
		password = password + numbers[number]
	
	return password

print "Please choose a password below\n"

for i in range(10):
		print make_password(6,2)
		print make_password(8,3)
		print make_password(10,4)