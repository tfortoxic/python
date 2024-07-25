try:
	l = [1,2,3,4,5]
	i = int(input("enter a index"))
	print(l[i])
except:
	print( "index error")
	
finally:
	print("program has been executed")