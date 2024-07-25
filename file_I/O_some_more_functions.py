#readlines() funtion is use to read line from a file 
f = open("shreevai2.txt",'w')

f.write("Beneath the moon's soft silver gleam, \nDreams take flight on starlit stream, \nIn whispers of the night's embrace,\nA world of wonder, time and space.")


f.close()
f = open("shreevai2.txt",'r')
while  True:
	line = f.readlines()
	if not line:
		break
	print(line)

f.close()
#writelines() 
f = open("shreevai2.txt",'w')
lines = ['line1','line2','line3']
f.writelines(lines)
f.close()
