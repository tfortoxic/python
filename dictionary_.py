#lets make a dictionary for employee name corresponding to employee id

dict = {122:"shree", 123:"biplop", 124 :"debraj", 125 :"ronish"
}
print(dict)

#dictinary values can be accsed using corresdonding iteration
print(dict[122])
print(dict[123])
print(dict[124])
print(dict[125])

#it can be accsed using for loop
for key  in dict.keys():
	print("this is using loop")
	print(dict[key])
	
