def combine(a, b):
	arg1 = a
        arg2 = b

        return '<' + str(arg1 + " " + arg2) + ">"

if __name__ == "__main__":
	print combine("aaa", "bbb")  # prints <aaa bbb>
