"""
00 01 02
10 11 12
20 21 22

left-diagonal: i == j
right-diagonal: i + j == len(arr) - 1
"""

def diagonalDifference(arr):
    size = len(arr)
    sum_left_diagonal = 0
    sum_right_diagonal = 0
    
    for i in range(size): 
        sum_left_diagonal += arr[i][i]
        
    for i in range(size):
        sum_right_diagonal += arr[i][size - 1 - i]
        
    return abs(sum_left_diagonal - sum_right_diagonal)
