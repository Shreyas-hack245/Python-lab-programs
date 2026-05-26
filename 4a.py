def sum_even_product_odd(numbers):

    sum_even = 0
    product_odd = 1

    for num in numbers:

        if num % 2 == 0:
            sum_even += num

        else:
            product_odd *= num

    return sum_even, product_odd

n = int(input("Enter n: "))

num_list = []

for i in range(n):
    num = int(input("Enter the elements: "))
    num_list.append(num)

sum, product = sum_even_product_odd(num_list)

print("Odd product =", product, "Even sum =", sum)