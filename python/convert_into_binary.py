def convert_into_binary(num):
    reminder = ""
    while num:
        remainder = num % 2
        num = num // 2
        reminder += str(remainder)       
    print(reminder[::-1])
decm = int(input("Enter a number to convert into binary: "))
convert_into_binary(decm)
