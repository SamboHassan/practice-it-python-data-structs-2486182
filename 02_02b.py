"""
Palindrone

1, Popping from either side
2, Tacocat
3, popleft()
4, pop()

"""

from collections import deque


def check_palindrone(word):
    d = deque()
    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
    return True


def main():
    # add code here
    word = "tocacat"
    print(check_palindrone(word))
    return


if __name__ == "__main__":
    main()
