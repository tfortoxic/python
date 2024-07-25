#continue statnent skips the part of an loop
print("we are using continue statment here :")
for i in range (12):
	if (i%2==0):
		continue
	else:
		print(i)
	
#break statement is use to break out of the looop 
print("we are using break statment here:")
for k in range (0 , 30):
	if (k==15):
		break
	else:
		print(k)	