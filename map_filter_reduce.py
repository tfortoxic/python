# map()  function is used to apply a given function to all items in an input list (or any iterable) and return an iterator that produces the results. It takes two parameters: the function to apply and the iterable to apply the function to.

'''
its exampl is given below

  '''
  
def cube(x):
	return x*x*x
lit = [2,3,4,5]

list2 = list(map(cube,lit))

print("cube of every items in the list are below:\n")

print(list2)

#filter() In Python, the filter() function is used to filter elements of an iterable (like a list, tuple, etc.) based on a function that tests each element for a condition. It constructs an iterator from elements of the iterable for which the function returns true.
nlist = [2,3,4,5,6,7,8,9]
def filter_function(a):
	return a>4
nlist = filter(filter_function, nlist)

print(nlist)

#or


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered_numbers)