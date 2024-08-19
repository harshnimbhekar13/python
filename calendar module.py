#importing calendar module 
import calendar()
yy = year
mm = month

yy = int (input("Enter Year :").format(year))
mm = int (input("Enter Month :").format(month))

print(calendar.month(yy,mm))