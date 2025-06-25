import sys

def main():
	argc = len(sys.argv)
	argv = sys.argv
	if (argc > 2):
		print(f"AssertionError: more than one argument is provided")
		return(1)
	
	if argc == 1:
		return
	
	try:
		num = int(argv[1])
		if (num % 2 == 0):
			print(f"I'm Even.")
		else:
			print(f"I'm Odd.")
	except ValueError:
		print("AssertionError: argument is not an integer")
		return 1



if __name__ == "__main__":
	main()