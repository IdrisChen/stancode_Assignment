"""
File: prime_checker.py
Name:Austin Chen
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
Q = -100

def main():
	"""
	TODO:
	"""
	print('Welcome to the prime checker!')
	ans = 0
	while True:
		ans = int(input('n: '))
		i = 2
		if ans == Q:
			print('Have a good one!')
			break
		else:
			while ans % i != 0:
				i += 1
			if i == ans:
				print(str(ans)+' is a prime number.')
			else:
				print(str(ans)+' is not a prime number.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
