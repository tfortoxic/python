#fibonacchi sequence using 

def fibo(fib):
	
	if fib<= 1:
		return 1 
	else :
		return fibo(fib-1) + fibo(fib-2)

fib = int(input("enter a number to create fibonachi sequence"))

for i in range(fib):
	print(fibo(i))


		