#if a string is palendrom
str = input("enter a word to check if it is palendrom\n")
str2 = "".join(reversed(str))
#print(str2)
if (str == str2):
	print(str + " is a palendrom")
else:
	print(str + " is not a palendrom")