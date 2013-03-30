import string

def column_only(numcol, rownum):
	cell = []

        for i in range(numcol):
            cell = cell + [string.uppercase[i]+str(rownum)]

        return cell

if __name__ == "__main__":
	print column_only(5, 19) # prints a list ["A19", "B19", "C19", "D19", "E19"]
