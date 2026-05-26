def isPrime(n):

    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

num = int(input("Enter number: "))

for i in range(2, num):

    if isPrime(i) and isPrime(num - i):
        print(num, "=", i, "+", num - i)
        break