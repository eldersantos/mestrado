
def fib(x):
	if (x == 1):
		return 1
	if (x == 0):
		return 1

	return fib(x-1) + fib(x-2)


if __name__ == "__main__":
	import sys
	print(fib(int(sys.argv[1])))