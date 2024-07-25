# Define a list of marks
marks = [12, 56, 33, 98, 12, 45, 1, 4]

# Iterate through the list using enumerate, which provides both index and value
for i, mark in enumerate(marks):
    # Print the current mark from the list
    print(mark)
    
    # Check if the current index is 3
    if i == 3:
        # If it is index 3, print a message indicating so
        print("This is index no 3")
        
#you can start from the enumurate value of your choice
#using start