import random

wordList = ("Amp","Frown","Winner")

allchar = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z", "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

numlist = ("1","2","3","4","5","6","7","8","9","0")

def make_password():
	password = ""
	
	word = random.randint(0,2)
	password = password + wordList[word]
	
	for i in range(10-len(wordList[word])-1):
		letter = random.randint(0, 51)
		password = password + allchar[letter] 
	
	number = random.randint(0,9)
	password = password + numlist[number]
	
	return password

print make_password()