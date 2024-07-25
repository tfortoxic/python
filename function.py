#function without return without argument
def grater ():
	if a<b:
		print("b is great")
	elif(a==b):
		print("a is equals to b")
	else:
		print("a is great")
		
a = float(input("enter a number. "))
b = float(input("enter a number."))
grater()

#function with return with argument
def smaller(a , b):
	if(a<b):
		print("a is the smallest")
	elif(a==b):
		print("a is equals to b")
	else:
		print("b is the smallest")
		
c = float(input("enter a number. "))
d = float(input("enter a number."))
smaller(c , d)

