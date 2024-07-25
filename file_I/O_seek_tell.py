#file I/O seek(),tell(),turncate()

#seek()
with open('myfile.txt','r') as f:
	
	print(type(f))
	f.seek(6)#skips the 1st six character
	print(f.tell())
	text = f.read()#reads the remaning character
	print(text)
	
	
#tell() is 
