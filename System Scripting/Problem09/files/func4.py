def combine(strdict):
	dictionary = ""

        for item in strdict:
            dictionary = dictionary + item + "," + strdict[item]+";"

        return dictionary

if __name__ == "__main__":
	print combine({"a":"b","c":"d"})  # prints "a,b;c,d;"
