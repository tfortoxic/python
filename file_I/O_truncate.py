#truncate() function is use to specify the size of file 
with open ('sample.txt','w') as f:
	f.write('hello world')
	f.truncate(5)
with open('sample.txt','r') as f:
	print(f.read())
f.close()