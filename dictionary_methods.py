#update(),clear(),pop(),popitem(),del(),

#update() is use to update one dictonary with value of another dictnory
# Dictionary
Dic = {
    "name": "Alice",
    "age": 25,
    "city": "Wonderland"
}

# Dictionary 1
Dic1 = {
    "animal": "lion",
    "color": "yellow",
    "habitat": "savannah"
}

Dic.update(Dic1)
print("this is an updated verson of Dictnory\n",Dic)

#clear() is use to clear a dictnory
dic3 = { "animal": "lion",
    "color": "yellow",
    "habitat": "savannah"
}

dic3.clear()

print("this is an empty dictonary  after clearing it \n")
print(dic3)

#we can create an empty dictonary as well 
empt = {} 
print("this is an empty dictonary")
print(empt)

#pop() method of dictonary is use to pop a choosen value from dictonary

# Dictionary for Apple
apple_dictionary = {
    "color": "red",
    "taste": "sweet",
    "nutrients": ["vitamin C", "fiber"],
    "origin": "Various regions worldwide"
}
apple_dictionary.pop("color")
print(apple_dictionary)

#popitem( )
print("this is the last item from the dicttnary:",apple_dictionary.popitem())

#del()




