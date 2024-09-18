num1 =float(input("Enter a First Number : "))
num2 =float(input("Enter a Second Number : "))
num3 =float(input("Enter a Third Number : "))

if(num1 < num2 ) and (num1 <= num3):
    Smallest = num1
elif (num2 <= num1 ) and (num2 <= num3):
    Smallest = num2
else:
    Smallest = num3
    
print("The Smallest Number is : ",Smallest)