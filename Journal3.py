'''
 Write a Python program that defines a function f(x) 
 that returns x**3 + 8. In the main function of the 
 program, call f(x) with x = 9 and print the result.  
 Use an if statement that executes if the result is 
 larger than 27 and prints “YAY!”.

 What I have tested:
 It is calling the f(x) subruten it is just not changing x.
 The 'if' statment is also working but since it is not chanign x
 it is it not met.
 '''

def f(x):
	# I don't know how to have it return to x
	return x**3+8     #if x = 9 output should be 737

def main():

	x = 9
	y = f(x)
	
	print(y)

	if(y>27):
		print('YAY!')
	

if __name__ == '__main__':
	main()
