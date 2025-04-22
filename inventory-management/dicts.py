"""Functions to keep track and alter inventory."""


def create_inventory(items: list) -> dict:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    new_dict = {}

    for item in items:
        amount = items.count(item)
        new_dict[item] = amount

    return new_dict


def add_items(inventory: dict, items: list) -> dict:
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    for item in items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory


def decrement_items(inventory: dict, items: list) -> dict:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items:
        if item in inventory.keys():
            if inventory[item] != 0:
                inventory[item] -= 1

    return inventory


def remove_item(inventory: dict, item: str) -> dict:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    if item not in inventory.keys():
        return inventory
    
    inventory.pop(item)
    return inventory


def list_inventory(inventory: dict) -> list[tuple]:
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    keys_to_remove = []

    for key in inventory.keys():
        if inventory[key] == 0:
            keys_to_remove.append(key)
    
    for key in keys_to_remove:
        inventory.pop(key)
    
    inventory_in_list = list(inventory.items())

    return inventory_in_list
