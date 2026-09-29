# Check whether a triangle is right-angled using the Pythagoras theorem

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("The triangle is right-angled.")
else:
    print("The triangle is not right-angled.")
