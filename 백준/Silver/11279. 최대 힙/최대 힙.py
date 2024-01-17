import heapq
import sys
input = sys.stdin.readline

N = int(input())
max_heap = []

for i in range(N):
    x = (int(input().strip()))

    if x == 0:
        if max_heap:
            max_value = heapq.heappop(max_heap)
            print(max_value[1])
        else:
            print(0)
    else:
        heapq.heappush(max_heap, (-x, x))