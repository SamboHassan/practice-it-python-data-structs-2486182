"""
Doing Inventory

1, Get the inventory into a counter object
2, Use the subtraction method
3, Add using the update method provided by Counter

"""

from collections import Counter


def main():
    # Add code here
    inventory = Counter(STA001=10, SAL002=20, ENT004=13)
    # sell 5 starters, 3 salads, and 3 entrees
    sales_this_week = Counter(STA001=5, SAL002=3, ENT004=3)
    inventory = inventory - sales_this_week
    print(inventory)

    # make 9 more starters and 1 more entree
    inventory_in = {"STA001": 9, "SAL002": 1}
    inventory.update(inventory_in)
    print(inventory)


if __name__ == "__main__":
    main()
