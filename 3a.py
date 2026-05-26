def collatz(n):

    if n % 2 == 0:
        return n // 2

    else:
        return 3 * n + 1

num = int(input("Enter number: "))

while num != 1:
    print(num, end=" ")
    num = collatz(num)

print(1)