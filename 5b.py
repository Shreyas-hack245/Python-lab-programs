def displayInventory(inventory):

    total = 0

    print("Inventory:")

    for item, count in inventory.items():
        print(count, item)
        total = total + count

    print("Total number of items:", total)


def addToInventory(inventory, addedItems):

    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1

    return inventory


inventory = {
    'arrow': 12,
    'gold coin': 42,
    'rope': 1,
    'torch': 6,
    'dagger': 1
}

addedItems = ['gold coin', 'dagger',
              'gold coin', 'gold coin', 'ruby']

inventory = addToInventory(inventory, addedItems)

displayInventory(inventory)