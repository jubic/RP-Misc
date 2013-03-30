import string

def column_only(numcol, rownum):
	ranges = []
	l = string.uppercase
	for i in range(numcol):
		ranges.append(l[i] + str(rownum))
	return ranges

if __name__ == "__main__":
	print column_only(5, 19)
