"""
Recent Orders
You want to keep track of the last 3 you ordered from Nadia and only the last 5 foods
How can you accomplish that with python using collection modules

1, Create a deque
2, append food to it
3, set the max lengh property when you create your deque

"""
from collections import deque


def main():
    foods = deque(maxlen=5)
    foods.append("STA001")  # we can append one at a time
    ordered_foods = ["DES003", "STA002", "ENT004", "ENT001"]
    foods.extend(ordered_foods)  # we can extend multiple
    print(foods)
    foods.append("DES002")
    print(foods)
    foods.appendleft("DES005")
    print(foods)
    return


if __name__ == "__main__":
    main()
