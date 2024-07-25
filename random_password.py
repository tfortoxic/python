import random
lower=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols =['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(lower)
print(upper)
print(symbols)
print(numbers)
lenth = int(input("enter the lenth of password"))
all= lower+upper+symbols+numbers
random_passwod = ''.join(random.choice(all)for i in range(lenth))
'''random.shuffle(random_passwod)'''
print(random_passwod)
