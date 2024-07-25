#variable/globle_variable/local_variable

#example
y=5 #y is a globle variable becouse its ouside the function and can be accesed without using function or outside the function
def myfunc():
	x = 10
	print("local variable is: x",x)
myfunc()
print("globle variable is :y ",y)

#globle variable can be accsed inside a function using globle keyword