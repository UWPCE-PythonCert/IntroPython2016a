#!/usr/bin/env python3
def FizBuz(n):
    """ FizBuz """

    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print('FizBuz')
        elif i % 3 == 0:
            print('Fiz')
        elif i % 5 == 0:
            print('Buz')
        else:
            print(i)

if __name__ == '__main__':
	FizBuz(100)
