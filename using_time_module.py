import time
time_stamp = time.strftime('%H,%M,%S')
print("It's "  + time_stamp + "O'clock")
#pulling time from time module hour,m8nute,second
hour = int(time.strftime('%H'))
b = int(time.strftime('%M'))
c = int(time.strftime('%S'))

print(hour)
print(b)
print(c)

if(hour>=4 and hour<=9):
	print("!!!!! good morning sir !!!!!")
elif(hour>9 and hour<=14):
	print("!!!!!! good afternoon sir/mam !!!!!")
elif(hour>14 and hour<19):
	print("!!!!! good evening sir/mam !!!!!")
else:
	print("!!!!! good night sir/mam !!!!")


