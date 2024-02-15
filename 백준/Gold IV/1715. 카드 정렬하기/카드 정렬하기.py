import heapq
import sys
input=sys.stdin.readline

def cards():
    N = int(input())
    numbers = [int(input()) for _ in range(N)]
    heapq.heapify(numbers)

    sum = 0

    if N == 1:
        return sum

    while len(numbers) > 1:
        temp = heapq.heappop(numbers) + heapq.heappop(numbers)
        sum += temp
        heapq.heappush(numbers, temp)

    return sum

# main
print(cards())