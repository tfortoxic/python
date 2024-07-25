a = float(input("enter a number"))
d = input("what calculation you want to do *,+,÷,%, **...  ")
b = float(input("enter a number"))

def addition ( ):
	c=a+b
	print(c)

def sub( ):
	c=a-b
	print(c)
	
def multi ( ):
	c=a*b
	print(c)
	
def reminder ( ):
	c=a%b
	print(c)
	
def power( ):
	c=a**b
	print(c)
	
def div ( ):
	c=a/b
	print(c)
	
if d== "+":
	addition()
if d== "-":
	sub()
if d == "*" :
	multi()
if d== "%":
	reminder()
if d== "**":
	power()
if d=="÷":
	div()
	