"""
File: quadratic_solver.py
Name:Austin Chen
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	TODO:
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter A: '))
	b = int(input('Enter B: '))
	c = int(input('Enter C: '))

	d = b**2 - 4*a*c
	if d > 0:
		y = math.sqrt(d)
		ans1 = float((-b+y/2*a))
		ans2 = float((-b-y)/2*a)
		print('Two roots: ' + str(ans1)+' , ' + str(ans2))
	elif d == 0:
		y = math.sqrt(d)
		ans1 = float((-b+y/2*a))
		print('One roots: ' + str(ans1))
	else:
		print('No real roots')





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
