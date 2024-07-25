#list is initialize by using [large brackers] 

list1 = [1, 6, 4, 8,3]
print(list1)

#append method of list is use to add value in last index of the list
list1.append(7)
print(list1)

#sort is use to sort the list in assending order

list1.sort()
print(list1)

#reverse is use to reverse the list 
list1.reverse()
print(list1)

#count iz use to count the element of list

print(list1.count(3))

#index is use to access specific element of list
print(list1.index(4))

#you can copy the existing list into an new list using copy method
nlist = list1.copy()
print(nlist)

#insert method is use to insert new value in specific index
list1.insert(1,800)
print(list1)

#extend is a method use to extend the list 
e =[1,2,3,4]
list1.extend(e)
print(list1)
