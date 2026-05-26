allGuests = {
    'Alice': {'apple': 5, 'pretzels': 12},
    'Bob': {'ham sandwiches': 3, 'apple': 2},
    'Carol': {'cups': 3, 'apple pies': 1}
}

def calculateTotal(allGuests, item):

    total = 0

    for key, value in allGuests.items():
        total = total + value.get(item, 0)

    return total

items_bought = ['apple', 'cups', 'cakes',
                'ham sandwiches', 'apple pies']

print("-" * 30)
print("Number of things being bought:")

for item in items_bought:
    print("-", item, calculateTotal(allGuests, item))

print("-" * 30)