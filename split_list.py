# Example array
arr = [4, 2, 7, 1, 9, 5, 3,4,9]

# Find the middle index
mid = len(arr) // 2
print("this is the middle of a array whis is: ",mid)

# Divide the array into two halves
left_half = arr[:mid]  # Subarray from index 0 to mid-1
right_half = arr[mid:]  # Subarray from mid to the end

print("Left half:", left_half)
print("Right half:", right_half)