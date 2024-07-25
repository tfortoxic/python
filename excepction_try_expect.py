
try:
	for i in range(1,12):
		print(i)
		
except excepction as e:
	print("sorry some error occred")

#try except is use to show the programmer about what error has occured suring execution 
try:
	num = int(input("enter a number"))
except ValueError:
	print("number entered is not intiger")
except IndexError:
	prrint("endex error")