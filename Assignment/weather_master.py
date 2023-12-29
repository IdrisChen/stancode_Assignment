"""
File: weather_master.py
Name:Austin Chen
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
Q = -100

def main():
	"""
	TODO:
	"""
	print('stanCode \"Weather Master 4.0\"!')
	ans = 0
	i = 1
	total = 0
	cold = 0
	ans = int(input('Next Temperature: (or ' + str(Q) + ' to quit)? '))
	total = ans
	if ans < 16:
		cold += 1
	if ans == Q:
		print('No temperatures were entered.')
	else:
		highest_temp = ans
		lowest_temp = ans
		while True:
			ans = int(input('Next Temperature: (or ' + str(Q) + ' to quit)? '))
			if ans == Q:
				break
			else:
				i += 1
				total = total + ans
				if ans > highest_temp:
					highest_temp = ans
				if ans < lowest_temp:
					lowest_temp = ans
				if ans < 16:
					cold += 1
		avg = total/i
		print('Highest temperature = '+str(highest_temp))
		print('Lowest temperature = '+str(lowest_temp))
		print('Average = '+str(float(total)))
		print(str(cold)+' cold day(s)')

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
