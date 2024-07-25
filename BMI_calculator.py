#An easy BMI calculator using python formula for BMI is wright/height ko square
weight = int(input("enter your weight "))
height_in_meter = float(input("enter your height"))

BMI = weight/(height_in_meter**2)

print("your BMI index is: ", BMI)

#here we used int() and float() function to pre set the input data type 