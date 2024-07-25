#set method is use to do some task within the selected sets such as union ,intersection, superset ,subset etc

set1 = {1,2,3,4}
set2 = {1,4,2,5,8}

print(set1,set2)

#union is use to find out union of 2 set just like in math a U b or in this program se1 U set2

setu = set1.union(set2)
print("union of set1 and set2 is: ",setu)

#intersection is use to see value that intersect the both sets 
cities = { "tokyo","kathmandu","hetauda","london" }
cities2 = { "tokyo","kathmandu","hetauda","london","pokhera" }
print(cities.intersection(cities2))#checking what intersets between element of cities and cities2



#update method of set is use to update one set with value of another set
set3 = {1,2,3,4}
set4 = {1,4,2,5,8,9,11}
set4.update(set4)
print("new updated set is ",set3,set4)