import sys
from typing import List, Any


def read() -> List[str]:
    return sys.stdin.readline().rstrip().split()


def write(value: Any):
    sys.stdout.write(str(value) + "\n")


def main():
    """
    input:
    2
    1 2
    3 4

    """
    t = int(read()[0])
    for _ in range(t):
        (a, b) = list(map(int, read()))
        write(f"{a}, {b}")

    value = read()
    if len(value) == 0: # EOF
        return


if __name__ == "__main__":
    main()
