def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("LCM is:", lcm(a, b))