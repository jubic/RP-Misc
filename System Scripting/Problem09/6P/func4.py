def combine(strdict):
	s = ""
	for (k,v) in strdict.items():
		s += k + "," + v + ";"
	return s

