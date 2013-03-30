def row_only(col, n):
	ranges = []
	for i in range(n):
		ranges.append(col + str(i+1))
	return ranges

if __name__ == "__main__":
	print row_only("G", 19)
