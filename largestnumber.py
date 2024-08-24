n1 = int(input("Enter a first Number : "))
n2 = int(input("Enter a second Number : "))
n3 = int(input("Enter a third Number : "))

if n1 > n2 and n1 > n3:
    largest = n1
elif n2 > n1 and n2 > n3:
    largest = n2
else:
    largest = n3
    
    largest = n3
    
print("Largest among {} {} and {}  largest number is  {}".format(n1,n2,n3,largest))