a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(str(a) + " is greater than " + str(b))

elif b > a:
    print(str(b) + " is greater than " + str(a))

else:
    print("Both are equal")