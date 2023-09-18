"""
Jesse loves cookies and wants the sweetness of some cookies to be greater than value . To do this, two cookies with the least sweetness are repeatedly mixed. This creates a special combined cookie with:

sweetness  Least sweet cookie   2nd least sweet cookie).

This occurs until all the cookies have a sweetness .

Given the sweetness of a number of cookies, determine the minimum number of operations required. If it is not possible, return .

1. put A into a priority queue: O(NlogN)
2. get the two least increasing their swetness: O(1) + O(logN) + O(1) = O(logN) # getMin, del, getMin
3. insert into priority queue: O(logN)
4. Check if the minimum value is greater than k: O(1)
5. repeat from 2. until len(A) != 1 : O(N)
6. result = -1

Time: O(NlogN) + O(logN) + O(logN) + O(1) + O(N) = O(NlogN) up to to 10^5 in 1 second
"""

import heapq

def cookies(k, A):
    heapq.heapify(A)
    iterations = 0
    while len(A) > 1:
        l1 = heapq.heappop(A)
        if l1 >= k:
            return iterations
        l2 = heapq.heappop(A)
        new_cookie = l1 + 2 * l2
        heapq.heappush(A, new_cookie)
        iterations += 1
    l1 = heapq.heappop(A)
    if l1 >= k:
        return iterations
    return -
