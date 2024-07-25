#strings in python can be decleared by using " " or ' ' for example
string = "hello"
string2 = 'world'
print(string)
print(string2)
#to check if both are string we will use type() function

print(type(string ))
print(type(string2))

#characters in strings can be accsed just like array. for example

string3 = "debraj"
print(string3[0])
print(string3[1])
print(string3[2])
print(string3[3])
print(string3[4])
print(string3[5])

#there are many pre defined function to change and manupulate string

#len() find out lenth of string 
#lower() lowercase
#upper() upper case
#replace() replace string
#strip() remove certain containt

str1 = "DeBrAj"

a = len(str1)
print("lenth or debraj is", a)

#reverse a string 
rev = "shree"
print(rev[::-1])# [start:stop:step] The slicing [::-1] means "start at the end of the string and end at position 0, moving with the step -1 (which means one step backwards)."