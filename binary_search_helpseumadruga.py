"""
Madruga finally got a job, that’s his big chance to pay the 14 months of rent that are late. He is a paper cutter and he is getting lots of money with this job.

Madruga will receive N rectangular strips of paper of 1 centimeter(cm) of width and C cm of length. The strips should be placed one beside the other so that their bases are aligned(check the image). The task is, with only one straight cut, parallel to the base, Madruga needs to make the sum of the areas of the cut strips equal to A cm².
"""


import sys
import functools

from typing import List


EPSILON = 1e-4


def cut(strips: List[float], height: float) -> float:
    area = 0.0
    for c in strips:
        if c <= height:
            break
        area += c - height
    return area


def search(strips: List[float], area: float) -> float:
    lo, hi = 0.0, strips[0]
    for _ in range(100):
    # while lo <= hi:
        mid = (lo + hi) / 2.0
        cutted_area = cut(strips, mid)
        if abs(cutted_area - area) < EPSILON:
            return mid
        elif cutted_area >= area:
            lo = mid
        else:
            hi = mid
    return lo


def main():
    while True:
        N, A = map(float, sys.stdin.readline().strip().split())
        if N == A and N == 0.0:
            break
        strips = list(map(float, sys.stdin.readline().strip().split()))

        area = sum(strips)
        if area < A:
            print("-.-")
            continue
        elif abs(area - A) < EPSILON:
            print(":D")
            continue

        strips = sorted(strips, reverse=True)
        result = search(strips, A)
        
        print(f"{result:.4f}")



if __name__ == "__main__":
    main()
