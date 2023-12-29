"""
File: hailstone.py
Name:Austin Chen
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    TODO:
    """
    print('This program computes Hailstone sequences.')
    print('')
    x = int(input('Enter a number: '))
    i = 0
    if x==1:
        print('It took 0 steps to reach 1.')
    else:
        while x != 1:

            if x%2==0:
                x /= 2
                print(str(int(2*x)) + ' is even, so I take half: '+str(int(x)))
            else:
                x = 3*x + 1
                print(str(int((x-1)/3)) + ' is odd, so I make 3n+1: '+str(int(x)))
            i += 1
        print('It took '+str(i)+' steps to reach 1.')




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
