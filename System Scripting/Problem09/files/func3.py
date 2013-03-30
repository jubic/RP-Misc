def combine(strlist):
	string = ""

        for item in strlist:
            string = string+"<"+str(item)+">"

        return string
    
if __name__ == "__main__":
	print combine(["one", "two"])  # prints "<one><two>"
