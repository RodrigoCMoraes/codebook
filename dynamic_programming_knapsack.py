"""
The "Destruction Cannon" game is very simple to be understood. You have been assigned a mission to destroy a castle, knowing that it has an integer number R, which represents the value of its max resistance. To accomplish your mission, you've received a cannon that is loaded with lead, and it has a maximum loading capacity K expressed in kilos. It is possible to exist pieces of lead with the same weight but with different destructive power and this is not so important. To each projectil that hit the castle, its destruction power amount must be subtracted from the castle total resistance.

Considering that the cannon can be loaded only once, respecting your limits of kilos, your task is to load the cannon with projectiles that do not exceed its load limit but do the most damage possible to know if the mission has been completed or not.
"""


import sys
from typing import List, Any, Tuple


sys.setrecursionlimit(10**9)


def read() -> List[int]:
    return sys.stdin.readline().rstrip().split()


def write(value: Any):
    sys.stdout.write(str(value) + "\n")


"""
    transactions: add, do not add
    states: item, sack weight
"""
def f(i:int, capacity:int, projectiles:List[Tuple[int, int]], states:List[List[int]]) -> int:
    if capacity < 0:
        return float("-inf")
    if i < 0:
        return 0
    if capacity == 0:
        return 0

    if states[i][capacity] != float("-inf"):
        return states[i][capacity]

    # do not add
    result1 = f(i - 1, capacity, projectiles, states)

    # add
    result2 = f(i - 1, capacity - projectiles[i][1], projectiles, states) + projectiles[i][0]

    states[i][capacity] = max(result1, result2)
    return states[i][capacity]


def main():
    t = int(read()[0])
    for _ in range(t):
        projectiles = []
        n = int(read()[0])
        for _ in range(n):
            (power, weight) = list(map(int, read()))
            projectiles.append(
                (power, weight)
            )
        k = int(read()[0])
        r = int(read()[0])

        states = [[float("-inf") for _ in range(k + 1)] for _ in range(n)]
        result = f(i=n - 1, capacity=k, projectiles=projectiles, states=states)

        message = "Falha na missao"
        if result >= r:
            message = "Missao completada com sucesso"
        write(message)


if __name__ == "__main__":
    main()
