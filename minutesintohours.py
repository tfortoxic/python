def findhour ():
	minutes=float(input("entertime in minute to convert into hour"))
	hours = minutes/60
	print(minutes,"minutes in hours is ", hours, "hours")
	
def findmin ():
	hour=float(input("entertime in hour to convert into hour"))
	minutes = hour*60
	print(hour ,"minutes in hours is ", minutes, "hours")

wanting_to = (input("enter a H to convert into hour and M to convert into minutes"))
if (wanting_to == "H" or wanting_to == "h" ):
	findhour()
elif(wanting_to == "M" or wanting_to == "m" ):
	findmin()
else:
	print("wrong input")
	