'''Demo of exception'''

def convert(s):
	try:
		return int(s)
	except (ValueError, TypeError):
		return -1

def concat(s):
	slist = ['12345', '654321']
	s = "".join(slist)
	return s