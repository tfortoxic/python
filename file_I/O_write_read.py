#file handeling and its basic functions input output,read,write append 
file = open('myfile.txt','w')#creating a file becouse myfile.txt dosenot exists 
file.write("shree is handsome")
6
file.close()#closing the file after writting the containt 

file = open('myfile.txt','r')#reopening file as file 

text = file.read()#storing the containt of file in text variable

print(text)
file.close()