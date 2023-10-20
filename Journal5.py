'''
Write a Python program that writes out a table 
of the function sin(x) vs. x, where x is tabulated 
between 0 and 2pi with a thousand entries. Follow the
basic Python program structure, including a main program function.
'''
import numpy as np


def main():
	n = 1000   #defines int
	x = np.arange(n,dtype=float) #defines array with n different numbers
	x *= 2.0*np.pi / float(n-1) #changes all 1000 numbers that create n to numbers between 0-2pi
	sin_x = np.sin(x)     #creates second array of the sin of x
	

if __name__ == '__main__':
	main()



