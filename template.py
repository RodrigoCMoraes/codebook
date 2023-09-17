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
        write("End Of File")

    rows, cols = 4, 5
    matrix = [[float("-inf") for _ in range(cols)] for _ in range(rows)]
    # avoid: [[float("-inf")] * cols] * rows
    # that way the rows will shared the tuples references
    write(f"rows: {len(matrix)}")
    write(f"cols: {len(matrix[0])}")


if __name__ == "__main__":
    main()
