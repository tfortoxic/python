# Define the range of numbers
start_number = 9760000000
end_number = 9870000000

# Define the file name
file_name = "numbers_ntc_70_82.txt"

# Open the file in write mode
with open(file_name, 'w') as file:
    # Write numbers to the file, each on a new line
    for num in range(start_number, end_number + 1):
        file.write(str(num) + '\n')

print("Numbers have been written to", file_name)
