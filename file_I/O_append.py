#append("") method is use to avoide overwritting of containt if adds new containt to a file with new memory address
f = open("shreevai.txt",'w')

f.write("Beneath the moon's soft silver gleam, \nDreams take flight on starlit stream, \nIn whispers of the night's embrace,\nA world of wonder, time and space.")

f.close()
#using the append function to add more to the file avoiding any overwrite
f = open("shreevai.txt",'a')
f.write("\nshree is don")
f.close()
#READING MODE
f = open("shreevai.txt",'r')
text = f.read()
print(text)
f.close()