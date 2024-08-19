a = int(input("Numerator "))
b = int(input("Denominator "))

try:
    ans = a / b
except ZeroDivisionError:
    print("Can't Divide By Zero")
    
else:
    print(ans)