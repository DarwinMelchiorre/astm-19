'''
Write a Python program that declares a class describing your 
favorite animal. Have the data members of the class represent the 
following physical parameters of the animal: length of the arms 
(float), length of the legs (float), number of eyes (int), does 
it have a tail? (bool), is it furry? (bool). Write an 
initialization function that sets the values of the data members 
when an instance of the class is created. Write a member function 
of the class to print out and describe the data members representing
the physical characteristics of the animal.
'''
class Fav_anm:
	def print(self):
		print(f"length of arms = {self.arms}")
		print(f"length of legs = {self.legs}")
		print(f"number of eyes = {self.eyes}")
		print(f"does it have a tail = {self.tail}")
		print(f"is it furry = {self.fur}")


	def __init__(self,lenarm=8.,lenleg=8.,numeye=8,tail=False,fur=False):
		self.arms  = lenarm
		self.legs  = lenleg
		self.eyes  = numeye
		self.tail  = tail
		self.fur     = fur


def main():
	animal = Fav_anm()
	animal.print()

if __name__ == '__main__':
	main()
