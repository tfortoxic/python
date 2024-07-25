def greeting ( ):
  print("hello!" + Name + " what would you like to order today?")
  print("we have:\ncapachini\nblack coffee\nanroti\nchole")
  order=input( )
  print("your " + order + "will be ready in a moment")
  price = 8
  how = input("how many you would like to order\n")
  total = price*int(how)
  print("your total is " + str(total))
  
print("what is your name")
Name=input( )
if Name == "debraj":
  debraj=input("are you evil debraj")
  if debraj == "yes":
    print("you are not welcome evil debraj")
  if debraj == "no":
    print("you are welcome here")
    greeting()

else:
	greeting()


