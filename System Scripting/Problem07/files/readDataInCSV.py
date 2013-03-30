import csv
#
f = open("students.csv")
data = csv.reader(f)
#
for row in data:
    # print every row as a list
    print row[0], ":", row[2]