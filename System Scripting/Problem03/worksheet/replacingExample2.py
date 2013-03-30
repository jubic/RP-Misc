import re
s = "Apple Orange"
p = re.sub("(\w+) (\w+)", r"\2 \1", s)
print p   # output: Orange Apple