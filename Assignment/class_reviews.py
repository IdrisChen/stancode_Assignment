"""
File: class_reviews.py
Name:Austin Chen
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

STOP = '-1'


def main():
    """
    TODO:
    """
    n101 = 0
    n001 = 0
    sum101 = 0
    sum001 = 0
    max101 = 0
    min101 = 200
    max001 = 0
    min001 = 200

    while True:
        cls = str(input('Which class? '))
        if cls.upper() == 'SC101':
            score = int(input('score: '))
            n101 += 1
            sum101 += score
            if min101 > score:
                min101 = score
            if max101 < score:
                max101 = score
        elif cls.upper() == 'SC001':
            score = int(input('score: '))
            n001 += 1
            sum001 += score
            if min001 > score:
                min001 = score
            if max001 < score:
                max001 = score
        elif cls == STOP:
            if min001 == 200 and min101 == 200:
                print('No class scores were entered')
                break
            else:
                for i in range(13):
                    print('=', end='')
                print('SC001', end='')
                for i in range(13):
                    print('=', end='')
                print('')
                if n001 == 0:
                    print('No score for SC001')
                else:
                    print('Max(001): ' + str(max001))
                    print('Min(001): ' + str(min001))
                    print('Avg(001): ' + str(sum001 / n001))

                    for i in range(13):
                        print('=', end='')
                    print('SC101', end='')
                    for i in range(13):
                        print('=', end='')
                    print('')
                    if n101 == 0:
                        print('No score for SC101')
                    else:
                        print('Max(101): ' + str(max101))
                        print('Min(101): ' + str(min101))
                        print('Avg(101): ' + str(sum101 / n101))
                break






# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
