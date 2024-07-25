#some other method of sets
#some useful methods of sets are isdisjoint(), issuperset(), issubset(), add(), remove(),discard(), pop(), del(), clear(), we will do somw program with all example and understand

# Creating set1 with three same values and two different values
set1 = {1, 2, 3, 3, 4}

# Creating set2 with three same values and two different values
set2 = {3, 4, 5, 5, 6}

#isdisjoint() is use to check if the 2 set donot contain the same value if they do it is false if they dont it is true

print(set1.isdisjoint(set2))#checking if set 1 is disjoint from set 2

#issubset( ) 
print(set1.issubset(set2))

# add() is use to add new element to a set
set1.add(5)

print(set1)

#remove() remove is use to remove element from a set
set1.remove(5)
print(set1)

#discard()
set1.discard(1)
print(set1)

#pop() is use to pop random value from set
print(set1.pop())

#del( ) is use to  delete a value from set 

del set1
#print(set1)

#clear() use to clear a set
set2.clear()
print(set2)