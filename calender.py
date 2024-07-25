import calendar

yy = int(input(print("which year calender you want")))


for i in range (1,12):
  if (i<=12):
    mm = i
    print(calendar.month(yy,mm))