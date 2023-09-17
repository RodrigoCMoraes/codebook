"""
A beginner investor wants to learn how to invest in the stock market. As he does not have any experience, he selected one company and followed daily the value of the stock during N days. At the end, he wondered how much money he would have won if he had invested during the time he followed the stock value. To be honest, the investor is multi billionaire and has a lot of money, enough to buy any amount of stock actions of the company. However, as he is very careful with his investments, he decided that he would never have more than one stock of the company.

To cover his costs, the stockbroker charges a fixed rate of C dollars for every stock purchase.

You have to calculate the maximum profit that the investor could have won investing during the N days, having also the option of not to invest any money.
"""


import sys
from typing import List, Any


sys.setrecursionlimit(10**9)


def read() -> List[str]:
    return sys.stdin.readline().rstrip().split()


def write(v: Any):
    sys.stdout.write(str(v) + "\n")


def f(day: int, has: int, charge: int, price: List[int], state: List[List[int]]) -> int:
    if day == len(price):
        return 0

    if state[has][day] != float("-inf"):
        return state[has][day]

    if has:
        do_nothing = f(day + 1, 1, charge, price, state)
        sell = f(day + 1, 0, charge, price, state) + price[day]
        state[has][day] = max(do_nothing, sell)
        return state[has][day]

    do_nothing = f(day + 1, 0, charge, price, state)
    buy = f(day + 1, 1, charge, price, state) - price[day] - charge
    state[has][day] = max(do_nothing, buy)
    return state[has][day]


def main():
    n, c = list(map(int, read()))
    price = list(map(int, read()))

    # Initialize state with separate lists for each row
    state = [[float("-inf")] * len(price) for _ in range(2)]  # two for 'has'
    result = f(day=0, has=0, charge=c, price=price, state=state)

    write(result)


if __name__ == "__main__":
    main()
